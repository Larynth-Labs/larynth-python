from typing import Literal

ExtractionFieldType = Literal["boolean", "date", "enum", "number", "string"]

EXTRACTION_FIELD_TYPE_VALUES: set[ExtractionFieldType] = {
    "boolean",
    "date",
    "enum",
    "number",
    "string",
}


def check_extraction_field_type(value: str) -> ExtractionFieldType:
    if value in EXTRACTION_FIELD_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EXTRACTION_FIELD_TYPE_VALUES!r}"
    )
