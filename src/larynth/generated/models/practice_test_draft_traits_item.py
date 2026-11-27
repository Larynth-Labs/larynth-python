from typing import Literal

PracticeTestDraftTraitsItem = Literal[
    "asks_for_person", "changes_mind", "in_a_hurry", "off_topic", "upset", "vague"
]

PRACTICE_TEST_DRAFT_TRAITS_ITEM_VALUES: set[PracticeTestDraftTraitsItem] = {
    "asks_for_person",
    "changes_mind",
    "in_a_hurry",
    "off_topic",
    "upset",
    "vague",
}


def check_practice_test_draft_traits_item(value: str) -> PracticeTestDraftTraitsItem:
    if value in PRACTICE_TEST_DRAFT_TRAITS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRACTICE_TEST_DRAFT_TRAITS_ITEM_VALUES!r}"
    )
