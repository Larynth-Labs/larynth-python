from typing import Literal

ListCatalogVoicesGender = Literal["female", "male", "neutral"]

LIST_CATALOG_VOICES_GENDER_VALUES: set[ListCatalogVoicesGender] = {
    "female",
    "male",
    "neutral",
}


def check_list_catalog_voices_gender(value: str) -> ListCatalogVoicesGender:
    if value in LIST_CATALOG_VOICES_GENDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_CATALOG_VOICES_GENDER_VALUES!r}"
    )
