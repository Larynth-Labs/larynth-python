from typing import Literal

CreateContactRequestRelationship = Literal["existing", "none"]

CREATE_CONTACT_REQUEST_RELATIONSHIP_VALUES: set[CreateContactRequestRelationship] = {
    "existing",
    "none",
}


def check_create_contact_request_relationship(
    value: str,
) -> CreateContactRequestRelationship:
    if value in CREATE_CONTACT_REQUEST_RELATIONSHIP_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_CONTACT_REQUEST_RELATIONSHIP_VALUES!r}"
    )
