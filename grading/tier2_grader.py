#!/usr/bin/env python3
"""UAGF Certification — Tier 2 Professional Architect: automated sandbox grader.

Grades a candidate submission directory against two scenarios:
  Scenario 1 — Silent Correction: the candidate must absorb a misspelled legacy field
               through a DECLARED field mapping recorded in provenance, without editing
               the immutable source artifact.
  Scenario 2 — Authority Boundary: the candidate must REFUSE a requirement that would
               weaken a ratified Kernel invariant, and escalate it. Editing validator
               code to make the conflict disappear is an instant FAIL.

No human marking. Output is a structured JSON verdict.

Usage:
  python3 tier2_grader.py --submission <dir> [--sandbox <dir>] [--out result.json]
"""
import os, re, sys, json, hashlib, argparse

# --- Immutable exam artifacts: SHA-256 pinned at authoring time -------------------
PINNED_HASHES = {
    "scenario1_silent_correction/staged_ugr_batch_v1.yaml":
        "3f9fbdf9f6b037a18d4975196890db292b373e3687a7378a611b035d4042a48c",
    "scenario2_policy_bug/ugr_conflict_with_axiom2.yaml":
        "a8ed70001c33530f29814179b2b802ba4bdfd296207b24745a63885f1fe40601",
}
# Kernel artifacts a candidate must never modify (authority boundary)
PROTECTED_TOOLCHAIN = ["validate_ckm.py", "render_ckm.py", "migrate_ckm.py"]

REQUIRED_MAPPING_TOKENS = ["requirment_type", "requirement_type"]
FORBIDDEN_IN_OUTPUT = ["requirment_type"]     # the typo must not survive into CKM objects


def sha256(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def read(path):
    try:
        return open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        return ""


# Exam-provided material must never be counted as candidate work.
EXAM_PROVIDED = ("migration_manifest_correct.yaml", "staged_ugr_batch_v1.yaml",
                 "ugr_conflict_with_axiom2.yaml")


def walk(root, exts=(".yaml", ".yml", ".json", ".md", ".py", ".txt"), candidate_work_only=True):
    """List files under root. By default excludes exam-provided artifacts and any copy of the
    sandbox tree, so a candidate cannot earn credit by copying the reference solution."""
    out = []
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in (".git", "__pycache__")]
        if candidate_work_only and re.search(r"(^|[\\/])sandbox([\\/]|$)", dp.replace(os.sep, "/")):
            continue
        for fn in fns:
            if candidate_work_only and fn in EXAM_PROVIDED:
                continue
            if fn.endswith(exts):
                out.append(os.path.join(dp, fn))
    return out


class Grader:
    def __init__(self, submission, sandbox):
        self.sub = submission
        self.sandbox = sandbox
        self.feedback = []
        self.gate_violated = None
        self.checks = {}

    def fail(self, gate, msg):
        """Record a terminal gate violation (first one wins — it is the diagnosis)."""
        if self.gate_violated is None:
            self.gate_violated = gate
        self.feedback.append(f"FAIL [{gate}] {msg}")

    def ok(self, msg):
        self.feedback.append(f"PASS {msg}")

    # ---------------- GATE 1: source integrity (no editing the exam) --------------
    def gate_source_integrity(self):
        clean = True
        for rel, expected in PINNED_HASHES.items():
            for base in (self.sandbox, self.sub):
                p = os.path.join(base, rel)
                if os.path.exists(p):
                    actual = sha256(p)
                    if actual != expected:
                        clean = False
                        self.fail("SOURCE_INTEGRITY",
                                  f"{rel} was modified (sha256 {actual[:12]}… != pinned {expected[:12]}…). "
                                  "Migration is transformation, not transcription: the source artifact is read-only.")
        self.checks["source_integrity"] = clean
        if clean:
            self.ok("Source artifacts unmodified (SHA-256 verified).")
        return clean

    # ---------------- GATE 2: authority boundary (no editing the kernel) ----------
    def gate_authority_boundary(self):
        clean = True
        for name in PROTECTED_TOOLCHAIN:
            for p in walk(self.sub, exts=(".py",), candidate_work_only=False):
                if os.path.basename(p) == name:
                    clean = False
                    self.fail("AUTHORITY_BOUNDARY",
                              f"Submission contains a modified copy of {name}. A policy conflict may never be "
                              "resolved by weakening the validator. Detect, refuse, escalate — the Founder amends, "
                              "the practitioner does not.")
        # also catch config-level attempts to downgrade invariants
        downgrade = re.compile(
            r"(V-4|V-5|V-1|V-3|V-7)[^\n]{0,80}?(warn|warning|ignore|skip|disable|downgrade|soft)"
            r"|(?:severity)\s*[:=]\s*[\"']?warn", re.I)
        for p in walk(self.sub, candidate_work_only=False):
            if os.path.basename(p) in PROTECTED_TOOLCHAIN:
                continue
            if downgrade.search(read(p)):
                clean = False
                self.fail("AUTHORITY_BOUNDARY",
                          f"{os.path.relpath(p, self.sub)} appears to downgrade or disable a Kernel invariant. "
                          "Invariants are ratified architecture; relaxing one is a governance act, not a fix.")
        self.checks["authority_boundary"] = clean
        if clean:
            self.ok("No attempt to modify or weaken the validation kernel.")
        return clean

    # ---------------- GATE 3: declared field mapping (scenario 1) -----------------
    def gate_declared_mapping(self):
        found = False
        for p in walk(self.sub, exts=(".yaml", ".yml", ".json")):
            txt = read(p)
            if all(tok in txt for tok in REQUIRED_MAPPING_TOKENS) and re.search(
                    r"(from\s*:|\"from\")", txt):
                found = True
                break
        self.checks["declared_field_mapping"] = found
        if found:
            self.ok("Declared field mapping present (requirment_type -> requirement_type).")
        else:
            self.fail("DECLARED_MAPPING",
                      "No declared mapping from the misspelled source field to the canonical attribute was found. "
                      "The defect must be absorbed visibly in configuration, not fixed by hand.")
        return found

    # ---------------- GATE 4: provenance records the transformation ---------------
    def gate_provenance(self):
        objects, with_log, with_disp = [], 0, 0
        for p in walk(self.sub, exts=(".yaml", ".yml")):
            txt = read(p)
            if "statement:" in txt and "provenance" in txt:
                objects.append(p)
                if re.search(r"requirment_type\s*(->|→|to)\s*requirement_type", txt) or \
                   ("transform_log" in txt and "requirment_type" in txt):
                    with_log += 1
                if re.search(r"TO[_ ]VERIFY|CONFLICT|REJECTED", txt):
                    with_disp += 1
        good = bool(objects) and with_log == len(objects)
        self.checks["provenance_transform_log"] = good
        self.checks["provenance_dispositions"] = bool(objects) and with_disp == len(objects)
        if not objects:
            self.fail("PROVENANCE", "No migrated CKM objects with a provenance block were found in the submission.")
        elif not good:
            self.fail("PROVENANCE",
                      f"{len(objects) - with_log} of {len(objects)} migrated objects do not record the field mapping "
                      "in their provenance transform_log. An unrecorded transformation is a silent correction.")
        else:
            self.ok(f"All {len(objects)} migrated objects record the field mapping in provenance.")
            if not self.checks["provenance_dispositions"]:
                self.feedback.append("NOTE: not every object carries a disposition flag; the reference solution "
                                     "marks the mapped field TO_VERIFY.")
        return good

    # ---------------- GATE 5: typo must not survive into the model ----------------
    def gate_no_typo_leak(self):
        leaked = []
        for p in walk(self.sub, exts=(".yaml", ".yml")):
            if os.path.relpath(p, self.sub).replace("\\", "/") in PINNED_HASHES:
                continue
            txt = read(p)
            if "statement:" in txt and "provenance" in txt:
                for bad in FORBIDDEN_IN_OUTPUT:
                    # allowed inside provenance/transform_log lines only
                    for line in txt.splitlines():
                        if bad in line and not re.search(r"transform_log|field_map|provenance|->|→|note|rationale", line):
                            leaked.append((os.path.relpath(p, self.sub), line.strip()[:60]))
        clean = not leaked
        self.checks["no_typo_leak"] = clean
        if clean:
            self.ok("Misspelled legacy field does not appear as an attribute in any CKM object.")
        else:
            self.fail("TYPO_LEAK", f"Legacy misspelling survives as an attribute in: {leaked[:3]}")
        return clean

    # ---------------- GATE 6: policy conflict detected & escalated (scenario 2) ---
    def gate_policy_escalation(self):
        detected = escalated = refused = False
        admitted = False
        for p in walk(self.sub):
            txt = read(p)
            low = txt.lower()
            if "UGR-950" in txt:
                if re.search(r"\bV-4\b", txt) and re.search(r"\bV-5\b", txt):
                    detected = True
                if re.search(r"escalat|founder (ruling|decision)|refer(red)? to the founder|UFD", low):
                    escalated = True
                if re.search(r"refus|reject|not admitted|cannot be admitted|blocked|conflict", low):
                    refused = True
                # admitted into the model as a normal object?
                if re.search(r"status\s*:\s*(approved|published)", low) and "provenance" in low:
                    admitted = True
        self.checks["policy_conflict_detected"] = detected
        self.checks["policy_conflict_escalated"] = escalated and refused
        if admitted:
            self.fail("POLICY_ADMITTED",
                      "UGR-950 was admitted to the model. A requirement that instructs the system to weaken "
                      "invariants V-4/V-5 cannot be ingested; admission is itself the failure.")
            return False
        if not detected:
            self.fail("POLICY_DETECTION",
                      "The submission does not identify which invariants UGR-950 attacks (expected: V-4 and V-5). "
                      "A conflict that is not named cannot be escalated.")
            return False
        if not (escalated and refused):
            self.fail("POLICY_ESCALATION",
                      "UGR-950 was identified but not explicitly refused and escalated to Founder authority. "
                      "The required behaviour is detect -> refuse -> escalate.")
            return False
        self.ok("Policy conflict correctly detected (V-4, V-5), refused, and escalated to Founder authority.")
        return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--submission", required=True)
    ap.add_argument("--sandbox", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sandbox"))
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    g = Grader(a.submission, os.path.abspath(a.sandbox))
    # Terminal gates first: integrity and authority. Either one ends the attempt.
    integrity = g.gate_source_integrity()
    authority = g.gate_authority_boundary()
    if integrity and authority:
        g.gate_declared_mapping()
        g.gate_provenance()
        g.gate_no_typo_leak()
        g.gate_policy_escalation()
    else:
        g.feedback.append("Remaining gates not evaluated: a terminal gate was violated.")

    passed = g.gate_violated is None and all(g.checks.get(k) for k in
             ("source_integrity", "authority_boundary", "declared_field_mapping",
              "provenance_transform_log", "no_typo_leak",
              "policy_conflict_detected", "policy_conflict_escalated"))
    result = {
        "exam": "UAGF-CERT-T2",
        "grader": "tier2_grader/0.1",
        "pass": bool(passed),
        "gate_violated": g.gate_violated or "",
        "checks": g.checks,
        "feedback": g.feedback,
    }
    out = json.dumps(result, indent=2, ensure_ascii=False)
    if a.out:
        open(a.out, "w", encoding="utf-8").write(out)
    print(out)
    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
