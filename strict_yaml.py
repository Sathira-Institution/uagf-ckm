"""Strict YAML loading helpers for UAGF canonical data."""

from pathlib import Path
from typing import Any

import yaml


class StrictYamlLoader(yaml.SafeLoader):
    """SafeLoader that rejects duplicate mapping keys."""


def _construct_mapping(loader: StrictYamlLoader, node, deep: bool = False):
    mapping = {}
    seen = set()

    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)

        try:
            hash(key)
        except TypeError as exc:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"unhashable key: {key!r}",
                key_node.start_mark,
            ) from exc

        if key in seen:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"duplicate key: {key!r}",
                key_node.start_mark,
            )

        seen.add(key)
        mapping[key] = loader.construct_object(value_node, deep=deep)

    return mapping


StrictYamlLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_mapping,
)


def load_yaml_file(path: str | Path) -> Any:
    """Load one UTF-8 YAML file while rejecting duplicate keys."""
    file_path = Path(path)

    try:
        with file_path.open("r", encoding="utf-8") as handle:
            return yaml.load(handle, Loader=StrictYamlLoader)
    except yaml.YAMLError as exc:
        raise ValueError(f"Invalid YAML in {file_path}: {exc}") from exc


def load_yaml_text(text: str, source: str = "<string>") -> Any:
    """Load YAML text while rejecting duplicate keys."""
    try:
        return yaml.load(text, Loader=StrictYamlLoader)
    except yaml.YAMLError as exc:
        raise ValueError(f"Invalid YAML in {source}: {exc}") from exc
