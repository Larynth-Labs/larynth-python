from typing import Literal

UpdateContactRequestRelationship = Literal["existing", "none"]

UPDATE_CONTACT_REQUEST_RELATIONSHIP_VALUES: set[UpdateContactRequestRelationship] = {
    "existing",
    "none",
}


def check_update_contact_request_relationship(
    value: str,
) -> UpdateContactRequestRelationship:
    if value in UPDATE_CONTACT_REQUEST_RELATIONSHIP_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_CONTACT_REQUEST_RELATIONSHIP_VALUES!r}"
    )
