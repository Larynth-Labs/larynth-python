from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.number_kind import NumberKind, check_number_kind
from ..models.number_route_type import NumberRouteType, check_number_route_type
from ..models.number_source import NumberSource, check_number_source
from ..models.number_status import NumberStatus, check_number_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.forward_source import ForwardSource
    from ..models.number_branded import NumberBranded
    from ..models.number_cnam import NumberCNAM
    from ..models.number_usage import NumberUsage
    from ..models.number_verification import NumberVerification
    from ..models.routing_plan import RoutingPlan
    from ..models.schedule_summary import ScheduleSummary


T = TypeVar("T", bound="Number")


@_attrs_define
class Number:
    """
    Attributes:
        country (str):
        created_at (datetime.datetime):
        e164 (str):
        id (UUID):
        monthly_price_micro (int):
        route_type (NumberRouteType):
        status (NumberStatus):
        updated_at (datetime.datetime):
        assistant_id (UUID | Unset):
        branded (NumberBranded | Unset):
        cnam (NumberCNAM | Unset):
        forward_sources (list[ForwardSource] | Unset): Lines seen forwarding to this number (Diversion/History-Info)
        forward_to_e164 (str | Unset):
        kind (NumberKind | Unset):
        label (str | Unset):
        next_renewal_at (datetime.datetime | Unset):
        purchased_at (datetime.datetime | Unset):
        region (str | Unset):
        released_at (datetime.datetime | Unset):
        revision (int | Unset): Routing revision; send it back as If-Match on updateNumberRouting
        routing (RoutingPlan | Unset):
        schedule_summary (ScheduleSummary | Unset):
        sip_trunk_id (UUID | Unset):
        source (NumberSource | Unset): byo_sip numbers answer inbound only and never act as caller ID
        spam_screening (bool | Unset):
        usage (NumberUsage | Unset):
        verification (NumberVerification | Unset):
    """

    country: str
    created_at: datetime.datetime
    e164: str
    id: UUID
    monthly_price_micro: int
    route_type: NumberRouteType
    status: NumberStatus
    updated_at: datetime.datetime
    assistant_id: UUID | Unset = UNSET
    branded: NumberBranded | Unset = UNSET
    cnam: NumberCNAM | Unset = UNSET
    forward_sources: list[ForwardSource] | Unset = UNSET
    forward_to_e164: str | Unset = UNSET
    kind: NumberKind | Unset = UNSET
    label: str | Unset = UNSET
    next_renewal_at: datetime.datetime | Unset = UNSET
    purchased_at: datetime.datetime | Unset = UNSET
    region: str | Unset = UNSET
    released_at: datetime.datetime | Unset = UNSET
    revision: int | Unset = UNSET
    routing: RoutingPlan | Unset = UNSET
    schedule_summary: ScheduleSummary | Unset = UNSET
    sip_trunk_id: UUID | Unset = UNSET
    source: NumberSource | Unset = UNSET
    spam_screening: bool | Unset = UNSET
    usage: NumberUsage | Unset = UNSET
    verification: NumberVerification | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        country = self.country

        created_at = self.created_at.isoformat()

        e164 = self.e164

        id = str(self.id)

        monthly_price_micro = self.monthly_price_micro

        route_type: str = self.route_type

        status: str = self.status

        updated_at = self.updated_at.isoformat()

        assistant_id: str | Unset = UNSET
        if not isinstance(self.assistant_id, Unset):
            assistant_id = str(self.assistant_id)

        branded: dict[str, Any] | Unset = UNSET
        if not isinstance(self.branded, Unset):
            branded = self.branded.to_dict()

        cnam: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cnam, Unset):
            cnam = self.cnam.to_dict()

        forward_sources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.forward_sources, Unset):
            forward_sources = []
            for forward_sources_item_data in self.forward_sources:
                forward_sources_item = forward_sources_item_data.to_dict()
                forward_sources.append(forward_sources_item)

        forward_to_e164 = self.forward_to_e164

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        label = self.label

        next_renewal_at: str | Unset = UNSET
        if not isinstance(self.next_renewal_at, Unset):
            next_renewal_at = self.next_renewal_at.isoformat()

        purchased_at: str | Unset = UNSET
        if not isinstance(self.purchased_at, Unset):
            purchased_at = self.purchased_at.isoformat()

        region = self.region

        released_at: str | Unset = UNSET
        if not isinstance(self.released_at, Unset):
            released_at = self.released_at.isoformat()

        revision = self.revision

        routing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.routing, Unset):
            routing = self.routing.to_dict()

        schedule_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule_summary, Unset):
            schedule_summary = self.schedule_summary.to_dict()

        sip_trunk_id: str | Unset = UNSET
        if not isinstance(self.sip_trunk_id, Unset):
            sip_trunk_id = str(self.sip_trunk_id)

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        spam_screening = self.spam_screening

        usage: dict[str, Any] | Unset = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        verification: dict[str, Any] | Unset = UNSET
        if not isinstance(self.verification, Unset):
            verification = self.verification.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "country": country,
                "created_at": created_at,
                "e164": e164,
                "id": id,
                "monthly_price_micro": monthly_price_micro,
                "route_type": route_type,
                "status": status,
                "updated_at": updated_at,
            }
        )
        if assistant_id is not UNSET:
            field_dict["assistant_id"] = assistant_id
        if branded is not UNSET:
            field_dict["branded"] = branded
        if cnam is not UNSET:
            field_dict["cnam"] = cnam
        if forward_sources is not UNSET:
            field_dict["forward_sources"] = forward_sources
        if forward_to_e164 is not UNSET:
            field_dict["forward_to_e164"] = forward_to_e164
        if kind is not UNSET:
            field_dict["kind"] = kind
        if label is not UNSET:
            field_dict["label"] = label
        if next_renewal_at is not UNSET:
            field_dict["next_renewal_at"] = next_renewal_at
        if purchased_at is not UNSET:
            field_dict["purchased_at"] = purchased_at
        if region is not UNSET:
            field_dict["region"] = region
        if released_at is not UNSET:
            field_dict["released_at"] = released_at
        if revision is not UNSET:
            field_dict["revision"] = revision
        if routing is not UNSET:
            field_dict["routing"] = routing
        if schedule_summary is not UNSET:
            field_dict["schedule_summary"] = schedule_summary
        if sip_trunk_id is not UNSET:
            field_dict["sip_trunk_id"] = sip_trunk_id
        if source is not UNSET:
            field_dict["source"] = source
        if spam_screening is not UNSET:
            field_dict["spam_screening"] = spam_screening
        if usage is not UNSET:
            field_dict["usage"] = usage
        if verification is not UNSET:
            field_dict["verification"] = verification

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.forward_source import ForwardSource
        from ..models.number_branded import NumberBranded
        from ..models.number_cnam import NumberCNAM
        from ..models.number_usage import NumberUsage
        from ..models.number_verification import NumberVerification
        from ..models.routing_plan import RoutingPlan
        from ..models.schedule_summary import ScheduleSummary

        d = dict(src_dict)
        country = d.pop("country")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        e164 = d.pop("e164")

        id = UUID(d.pop("id"))

        monthly_price_micro = d.pop("monthly_price_micro")

        route_type = check_number_route_type(d.pop("route_type"))

        status = check_number_status(d.pop("status"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _assistant_id = d.pop("assistant_id", UNSET)
        assistant_id: UUID | Unset
        if isinstance(_assistant_id, Unset):
            assistant_id = UNSET
        else:
            assistant_id = UUID(_assistant_id)

        _branded = d.pop("branded", UNSET)
        branded: NumberBranded | Unset
        if isinstance(_branded, Unset):
            branded = UNSET
        else:
            branded = NumberBranded.from_dict(_branded)

        _cnam = d.pop("cnam", UNSET)
        cnam: NumberCNAM | Unset
        if isinstance(_cnam, Unset):
            cnam = UNSET
        else:
            cnam = NumberCNAM.from_dict(_cnam)

        _forward_sources = d.pop("forward_sources", UNSET)
        forward_sources: list[ForwardSource] | Unset = UNSET
        if _forward_sources is not UNSET:
            forward_sources = []
            for forward_sources_item_data in _forward_sources:
                forward_sources_item = ForwardSource.from_dict(
                    forward_sources_item_data
                )

                forward_sources.append(forward_sources_item)

        forward_to_e164 = d.pop("forward_to_e164", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: NumberKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_number_kind(_kind)

        label = d.pop("label", UNSET)

        _next_renewal_at = d.pop("next_renewal_at", UNSET)
        next_renewal_at: datetime.datetime | Unset
        if isinstance(_next_renewal_at, Unset):
            next_renewal_at = UNSET
        else:
            next_renewal_at = datetime.datetime.fromisoformat(_next_renewal_at)

        _purchased_at = d.pop("purchased_at", UNSET)
        purchased_at: datetime.datetime | Unset
        if isinstance(_purchased_at, Unset):
            purchased_at = UNSET
        else:
            purchased_at = datetime.datetime.fromisoformat(_purchased_at)

        region = d.pop("region", UNSET)

        _released_at = d.pop("released_at", UNSET)
        released_at: datetime.datetime | Unset
        if isinstance(_released_at, Unset):
            released_at = UNSET
        else:
            released_at = datetime.datetime.fromisoformat(_released_at)

        revision = d.pop("revision", UNSET)

        _routing = d.pop("routing", UNSET)
        routing: RoutingPlan | Unset
        if isinstance(_routing, Unset):
            routing = UNSET
        else:
            routing = RoutingPlan.from_dict(_routing)

        _schedule_summary = d.pop("schedule_summary", UNSET)
        schedule_summary: ScheduleSummary | Unset
        if isinstance(_schedule_summary, Unset):
            schedule_summary = UNSET
        else:
            schedule_summary = ScheduleSummary.from_dict(_schedule_summary)

        _sip_trunk_id = d.pop("sip_trunk_id", UNSET)
        sip_trunk_id: UUID | Unset
        if isinstance(_sip_trunk_id, Unset):
            sip_trunk_id = UNSET
        else:
            sip_trunk_id = UUID(_sip_trunk_id)

        _source = d.pop("source", UNSET)
        source: NumberSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_number_source(_source)

        spam_screening = d.pop("spam_screening", UNSET)

        _usage = d.pop("usage", UNSET)
        usage: NumberUsage | Unset
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = NumberUsage.from_dict(_usage)

        _verification = d.pop("verification", UNSET)
        verification: NumberVerification | Unset
        if isinstance(_verification, Unset):
            verification = UNSET
        else:
            verification = NumberVerification.from_dict(_verification)

        number = cls(
            country=country,
            created_at=created_at,
            e164=e164,
            id=id,
            monthly_price_micro=monthly_price_micro,
            route_type=route_type,
            status=status,
            updated_at=updated_at,
            assistant_id=assistant_id,
            branded=branded,
            cnam=cnam,
            forward_sources=forward_sources,
            forward_to_e164=forward_to_e164,
            kind=kind,
            label=label,
            next_renewal_at=next_renewal_at,
            purchased_at=purchased_at,
            region=region,
            released_at=released_at,
            revision=revision,
            routing=routing,
            schedule_summary=schedule_summary,
            sip_trunk_id=sip_trunk_id,
            source=source,
            spam_screening=spam_screening,
            usage=usage,
            verification=verification,
        )

        return number
