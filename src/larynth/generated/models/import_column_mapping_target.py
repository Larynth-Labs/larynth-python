from typing import Literal

ImportColumnMappingTarget = Literal[
    "attr",
    "consent_evidence",
    "first_name",
    "last_name",
    "phone",
    "relationship",
    "skip",
    "tag",
    "timezone",
]

IMPORT_COLUMN_MAPPING_TARGET_VALUES: set[ImportColumnMappingTarget] = {
    "attr",
    "consent_evidence",
    "first_name",
    "last_name",
    "phone",
    "relationship",
    "skip",
    "tag",
    "timezone",
}


def check_import_column_mapping_target(value: str) -> ImportColumnMappingTarget:
    if value in IMPORT_COLUMN_MAPPING_TARGET_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {IMPORT_COLUMN_MAPPING_TARGET_VALUES!r}"
    )
