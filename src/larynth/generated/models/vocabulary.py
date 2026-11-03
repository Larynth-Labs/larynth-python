from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pronunciation import Pronunciation


T = TypeVar("T", bound="Vocabulary")


@_attrs_define
class Vocabulary:
    """
    Attributes:
        keyterms (list[str] | Unset): Words to recognise, sent to the speech recognizer when its catalog row supports
            them
        pronunciations (list[Pronunciation] | Unset): How to say words in generated speech; transcripts keep the written
            word
    """

    keyterms: list[str] | Unset = UNSET
    pronunciations: list[Pronunciation] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        keyterms: list[str] | Unset = UNSET
        if not isinstance(self.keyterms, Unset):
            keyterms = self.keyterms

        pronunciations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pronunciations, Unset):
            pronunciations = []
            for pronunciations_item_data in self.pronunciations:
                pronunciations_item = pronunciations_item_data.to_dict()
                pronunciations.append(pronunciations_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if keyterms is not UNSET:
            field_dict["keyterms"] = keyterms
        if pronunciations is not UNSET:
            field_dict["pronunciations"] = pronunciations

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pronunciation import Pronunciation

        d = dict(src_dict)
        keyterms = cast(list[str], d.pop("keyterms", UNSET))

        _pronunciations = d.pop("pronunciations", UNSET)
        pronunciations: list[Pronunciation] | Unset = UNSET
        if _pronunciations is not UNSET:
            pronunciations = []
            for pronunciations_item_data in _pronunciations:
                pronunciations_item = Pronunciation.from_dict(pronunciations_item_data)

                pronunciations.append(pronunciations_item)

        vocabulary = cls(
            keyterms=keyterms,
            pronunciations=pronunciations,
        )

        return vocabulary
