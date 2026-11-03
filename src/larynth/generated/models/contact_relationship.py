from typing import Literal

ContactRelationship = Literal["existing", "none"]

CONTACT_RELATIONSHIP_VALUES: set[ContactRelationship] = {
    "existing",
    "none",
}


def check_contact_relationship(value: str) -> ContactRelationship:
    if value in CONTACT_RELATIONSHIP_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTACT_RELATIONSHIP_VALUES!r}"
    )
