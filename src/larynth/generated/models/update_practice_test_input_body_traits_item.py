from typing import Literal

UpdatePracticeTestInputBodyTraitsItem = Literal[
    "asks_for_person", "changes_mind", "in_a_hurry", "off_topic", "upset", "vague"
]

UPDATE_PRACTICE_TEST_INPUT_BODY_TRAITS_ITEM_VALUES: set[
    UpdatePracticeTestInputBodyTraitsItem
] = {
    "asks_for_person",
    "changes_mind",
    "in_a_hurry",
    "off_topic",
    "upset",
    "vague",
}


def check_update_practice_test_input_body_traits_item(
    value: str,
) -> UpdatePracticeTestInputBodyTraitsItem:
    if value in UPDATE_PRACTICE_TEST_INPUT_BODY_TRAITS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_PRACTICE_TEST_INPUT_BODY_TRAITS_ITEM_VALUES!r}"
    )
