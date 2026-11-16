from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.practice_test_source import PracticeTestSource, check_practice_test_source
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.practice_check import PracticeCheck


T = TypeVar("T", bound="PracticeTest")


@_attrs_define
class PracticeTest:
    """
    Attributes:
        assistant_id (UUID):
        created_at (datetime.datetime):
        id (UUID):
        must (list[PracticeCheck]): What must happen
        name (str):
        source (PracticeTestSource):
        updated_at (datetime.datetime):
        wants (str): What they want
        who (str): Who is calling
        caller_e164 (str | Unset): The number the agent sees as the caller; unset is the standard practice caller
        key (str | Unset): Stable id of a starter practice call
    """

    assistant_id: UUID
    created_at: datetime.datetime
    id: UUID
    must: list[PracticeCheck]
    name: str
    source: PracticeTestSource
    updated_at: datetime.datetime
    wants: str
    who: str
    caller_e164: str | Unset = UNSET
    key: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        assistant_id = str(self.assistant_id)

        created_at = self.created_at.isoformat()

        id = str(self.id)

        must = []
        for must_item_data in self.must:
            must_item = must_item_data.to_dict()
            must.append(must_item)

        name = self.name

        source: str = self.source

        updated_at = self.updated_at.isoformat()

        wants = self.wants

        who = self.who

        caller_e164 = self.caller_e164

        key = self.key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "assistant_id": assistant_id,
                "created_at": created_at,
                "id": id,
                "must": must,
                "name": name,
                "source": source,
                "updated_at": updated_at,
                "wants": wants,
                "who": who,
            }
        )
        if caller_e164 is not UNSET:
            field_dict["caller_e164"] = caller_e164
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.practice_check import PracticeCheck

        d = dict(src_dict)
        assistant_id = UUID(d.pop("assistant_id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = UUID(d.pop("id"))

        must = []
        _must = d.pop("must")
        for must_item_data in _must:
            must_item = PracticeCheck.from_dict(must_item_data)

            must.append(must_item)

        name = d.pop("name")

        source = check_practice_test_source(d.pop("source"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        wants = d.pop("wants")

        who = d.pop("who")

        caller_e164 = d.pop("caller_e164", UNSET)

        key = d.pop("key", UNSET)

        practice_test = cls(
            assistant_id=assistant_id,
            created_at=created_at,
            id=id,
            must=must,
            name=name,
            source=source,
            updated_at=updated_at,
            wants=wants,
            who=who,
            caller_e164=caller_e164,
            key=key,
        )

        return practice_test
