from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="Pronunciation")


@_attrs_define
class Pronunciation:
    """
    Attributes:
        say_as (str):
        word (str):
    """

    say_as: str
    word: str

    def to_dict(self) -> dict[str, Any]:
        say_as = self.say_as

        word = self.word

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "say_as": say_as,
                "word": word,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        say_as = d.pop("say_as")

        word = d.pop("word")

        pronunciation = cls(
            say_as=say_as,
            word=word,
        )

        return pronunciation
