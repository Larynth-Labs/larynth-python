from typing import Literal

ListBuilderPresetsDirection = Literal["inbound", "outbound", "web_test"]

LIST_BUILDER_PRESETS_DIRECTION_VALUES: set[ListBuilderPresetsDirection] = {
    "inbound",
    "outbound",
    "web_test",
}


def check_list_builder_presets_direction(value: str) -> ListBuilderPresetsDirection:
    if value in LIST_BUILDER_PRESETS_DIRECTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_BUILDER_PRESETS_DIRECTION_VALUES!r}"
    )
