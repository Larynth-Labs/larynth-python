from typing import Literal

ListNumbersCanCallOut = Literal["false", "true"]

LIST_NUMBERS_CAN_CALL_OUT_VALUES: set[ListNumbersCanCallOut] = {
    "false",
    "true",
}


def check_list_numbers_can_call_out(value: str) -> ListNumbersCanCallOut:
    if value in LIST_NUMBERS_CAN_CALL_OUT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_NUMBERS_CAN_CALL_OUT_VALUES!r}"
    )
