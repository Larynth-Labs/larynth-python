from typing import Literal

ListLiveModelsDirection = Literal["inbound", "outbound", "web_test"]

LIST_LIVE_MODELS_DIRECTION_VALUES: set[ListLiveModelsDirection] = {
    "inbound",
    "outbound",
    "web_test",
}


def check_list_live_models_direction(value: str) -> ListLiveModelsDirection:
    if value in LIST_LIVE_MODELS_DIRECTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_LIVE_MODELS_DIRECTION_VALUES!r}"
    )
