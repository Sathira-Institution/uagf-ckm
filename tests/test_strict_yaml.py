import pytest

from strict_yaml import load_yaml_file, load_yaml_text


def test_duplicate_yaml_key_is_rejected():
    with pytest.raises(ValueError, match="duplicate key"):
        load_yaml_text("label: first\nlabel: second\n")


def test_malformed_yaml_is_rejected():
    with pytest.raises(ValueError, match="Invalid YAML"):
        load_yaml_text("items: [broken\n")


def test_valid_yaml_is_loaded():
    result = load_yaml_text("id: DOM-TEST\ntier: 1\n")
    assert result == {"id": "DOM-TEST", "tier": 1}


def test_file_loader_uses_strict_loader(tmp_path):
    path = tmp_path / "duplicate.yaml"
    path.write_text("a: 1\na: 2\n", encoding="utf-8")

    with pytest.raises(ValueError, match="duplicate key"):
        load_yaml_file(path)
