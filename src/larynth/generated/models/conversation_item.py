from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.conversation_item_kind import (
    ConversationItemKind,
    check_conversation_item_kind,
)
from ..models.conversation_item_speaker import (
    ConversationItemSpeaker,
    check_conversation_item_speaker,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.call_transfer import CallTransfer
    from ..models.conversation_marker import ConversationMarker
    from ..models.conversation_tool import ConversationTool
    from ..models.turn_latency import TurnLatency


T = TypeVar("T", bound="ConversationItem")


@_attrs_define
class ConversationItem:
    """
    Attributes:
        at_ms (int): Offset from answered_at
        kind (ConversationItemKind):
        barged_in (bool | Unset):
        end_ms (int | Unset):
        latency (TurnLatency | Unset):
        marker (ConversationMarker | Unset):
        speaker (ConversationItemSpeaker | Unset):
        text (str | Unset):
        tool (ConversationTool | Unset):
        transfer (CallTransfer | Unset):
        truncated (bool | Unset): Realtime only: text over 4 KB was cut; fetch the conversation
        turn_index (int | Unset):
    """

    at_ms: int
    kind: ConversationItemKind
    barged_in: bool | Unset = UNSET
    end_ms: int | Unset = UNSET
    latency: TurnLatency | Unset = UNSET
    marker: ConversationMarker | Unset = UNSET
    speaker: ConversationItemSpeaker | Unset = UNSET
    text: str | Unset = UNSET
    tool: ConversationTool | Unset = UNSET
    transfer: CallTransfer | Unset = UNSET
    truncated: bool | Unset = UNSET
    turn_index: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        at_ms = self.at_ms

        kind: str = self.kind

        barged_in = self.barged_in

        end_ms = self.end_ms

        latency: dict[str, Any] | Unset = UNSET
        if not isinstance(self.latency, Unset):
            latency = self.latency.to_dict()

        marker: dict[str, Any] | Unset = UNSET
        if not isinstance(self.marker, Unset):
            marker = self.marker.to_dict()

        speaker: str | Unset = UNSET
        if not isinstance(self.speaker, Unset):
            speaker = self.speaker

        text = self.text

        tool: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tool, Unset):
            tool = self.tool.to_dict()

        transfer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transfer, Unset):
            transfer = self.transfer.to_dict()

        truncated = self.truncated

        turn_index = self.turn_index

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "at_ms": at_ms,
                "kind": kind,
            }
        )
        if barged_in is not UNSET:
            field_dict["barged_in"] = barged_in
        if end_ms is not UNSET:
            field_dict["end_ms"] = end_ms
        if latency is not UNSET:
            field_dict["latency"] = latency
        if marker is not UNSET:
            field_dict["marker"] = marker
        if speaker is not UNSET:
            field_dict["speaker"] = speaker
        if text is not UNSET:
            field_dict["text"] = text
        if tool is not UNSET:
            field_dict["tool"] = tool
        if transfer is not UNSET:
            field_dict["transfer"] = transfer
        if truncated is not UNSET:
            field_dict["truncated"] = truncated
        if turn_index is not UNSET:
            field_dict["turn_index"] = turn_index

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.call_transfer import CallTransfer
        from ..models.conversation_marker import ConversationMarker
        from ..models.conversation_tool import ConversationTool
        from ..models.turn_latency import TurnLatency

        d = dict(src_dict)
        at_ms = d.pop("at_ms")

        kind = check_conversation_item_kind(d.pop("kind"))

        barged_in = d.pop("barged_in", UNSET)

        end_ms = d.pop("end_ms", UNSET)

        _latency = d.pop("latency", UNSET)
        latency: TurnLatency | Unset
        if isinstance(_latency, Unset):
            latency = UNSET
        else:
            latency = TurnLatency.from_dict(_latency)

        _marker = d.pop("marker", UNSET)
        marker: ConversationMarker | Unset
        if isinstance(_marker, Unset):
            marker = UNSET
        else:
            marker = ConversationMarker.from_dict(_marker)

        _speaker = d.pop("speaker", UNSET)
        speaker: ConversationItemSpeaker | Unset
        if isinstance(_speaker, Unset):
            speaker = UNSET
        else:
            speaker = check_conversation_item_speaker(_speaker)

        text = d.pop("text", UNSET)

        _tool = d.pop("tool", UNSET)
        tool: ConversationTool | Unset
        if isinstance(_tool, Unset):
            tool = UNSET
        else:
            tool = ConversationTool.from_dict(_tool)

        _transfer = d.pop("transfer", UNSET)
        transfer: CallTransfer | Unset
        if isinstance(_transfer, Unset):
            transfer = UNSET
        else:
            transfer = CallTransfer.from_dict(_transfer)

        truncated = d.pop("truncated", UNSET)

        turn_index = d.pop("turn_index", UNSET)

        conversation_item = cls(
            at_ms=at_ms,
            kind=kind,
            barged_in=barged_in,
            end_ms=end_ms,
            latency=latency,
            marker=marker,
            speaker=speaker,
            text=text,
            tool=tool,
            transfer=transfer,
            truncated=truncated,
            turn_index=turn_index,
        )

        return conversation_item
