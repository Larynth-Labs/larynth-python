from typing import Literal

TransferDestinationMode = Literal["cold", "warm"]

TRANSFER_DESTINATION_MODE_VALUES: set[TransferDestinationMode] = {
    "cold",
    "warm",
}


def check_transfer_destination_mode(value: str) -> TransferDestinationMode:
    if value in TRANSFER_DESTINATION_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRANSFER_DESTINATION_MODE_VALUES!r}"
    )
