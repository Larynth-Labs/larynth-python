from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.workspace_tool_class import WorkspaceToolClass, check_workspace_tool_class
from ..models.workspace_tool_kind import WorkspaceToolKind, check_workspace_tool_kind
from ..models.workspace_tool_method import (
    WorkspaceToolMethod,
    check_workspace_tool_method,
)
from ..models.workspace_tool_status import (
    WorkspaceToolStatus,
    check_workspace_tool_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_invocation_summary import ToolInvocationSummary
    from ..models.tool_response_handling import ToolResponseHandling
    from ..models.tool_use import ToolUse
    from ..models.workspace_tool_args_schema import WorkspaceToolArgsSchema
    from ..models.workspace_tool_body_template import WorkspaceToolBodyTemplate
    from ..models.workspace_tool_bound import WorkspaceToolBound
    from ..models.workspace_tool_headers import WorkspaceToolHeaders
    from ..models.workspace_tool_query_template import WorkspaceToolQueryTemplate
    from ..models.workspace_tool_secret_headers import WorkspaceToolSecretHeaders


T = TypeVar("T", bound="WorkspaceTool")


@_attrs_define
class WorkspaceTool:
    """
    Attributes:
        args_schema (WorkspaceToolArgsSchema): Closed object schema, at most 16 properties and depth 3
        class_ (WorkspaceToolClass): fast answers without a filler line; slow plays one filler first
        created_at (datetime.datetime):
        description (str): Shown to the model
        id (UUID):
        kind (WorkspaceToolKind):
        method (WorkspaceToolMethod):
        name (str): Name the model calls
        revision (int):
        status (WorkspaceToolStatus):
        timeout_ms (int): fast 300 to 1500, slow 500 to 10000
        title (str):
        updated_at (datetime.datetime):
        url (str): https only, no user info; checked against private and reserved addresses
        used_by (list[ToolUse]):
        write (bool): Changes data: never retried
        body_template (WorkspaceToolBodyTemplate | Unset): JSON body with {{arg}} and {{call.field}} placeholders
        bound (WorkspaceToolBound | Unset): JSON pointer in the request to a call field the model cannot change:
            call_id, caller_e164, agent_e164, contact_id, campaign_id
        created_by (UUID | Unset): The user who created the tool; absent when an API key did
        created_by_api_key_id (UUID | Unset): The API key that created the tool, when no user did
        created_by_name (str | Unset):
        fallback_line (str | Unset): Spoken when the call fails
        headers (WorkspaceToolHeaders | Unset): Fixed headers; Authorization and Cookie need secret_headers
        last_invocation (ToolInvocationSummary | Unset):
        query_template (WorkspaceToolQueryTemplate | Unset): Query parameters with {{arg}} and {{call.field}}
            placeholders
        response (ToolResponseHandling | Unset):
        secret_headers (WorkspaceToolSecretHeaders | Unset): Header name to secret id
    """

    args_schema: WorkspaceToolArgsSchema
    class_: WorkspaceToolClass
    created_at: datetime.datetime
    description: str
    id: UUID
    kind: WorkspaceToolKind
    method: WorkspaceToolMethod
    name: str
    revision: int
    status: WorkspaceToolStatus
    timeout_ms: int
    title: str
    updated_at: datetime.datetime
    url: str
    used_by: list[ToolUse]
    write: bool
    body_template: WorkspaceToolBodyTemplate | Unset = UNSET
    bound: WorkspaceToolBound | Unset = UNSET
    created_by: UUID | Unset = UNSET
    created_by_api_key_id: UUID | Unset = UNSET
    created_by_name: str | Unset = UNSET
    fallback_line: str | Unset = UNSET
    headers: WorkspaceToolHeaders | Unset = UNSET
    last_invocation: ToolInvocationSummary | Unset = UNSET
    query_template: WorkspaceToolQueryTemplate | Unset = UNSET
    response: ToolResponseHandling | Unset = UNSET
    secret_headers: WorkspaceToolSecretHeaders | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        args_schema = self.args_schema.to_dict()

        class_: str = self.class_

        created_at = self.created_at.isoformat()

        description = self.description

        id = str(self.id)

        kind: str = self.kind

        method: str = self.method

        name = self.name

        revision = self.revision

        status: str = self.status

        timeout_ms = self.timeout_ms

        title = self.title

        updated_at = self.updated_at.isoformat()

        url = self.url

        used_by = []
        for used_by_item_data in self.used_by:
            used_by_item = used_by_item_data.to_dict()
            used_by.append(used_by_item)

        write = self.write

        body_template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body_template, Unset):
            body_template = self.body_template.to_dict()

        bound: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bound, Unset):
            bound = self.bound.to_dict()

        created_by: str | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = str(self.created_by)

        created_by_api_key_id: str | Unset = UNSET
        if not isinstance(self.created_by_api_key_id, Unset):
            created_by_api_key_id = str(self.created_by_api_key_id)

        created_by_name = self.created_by_name

        fallback_line = self.fallback_line

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        last_invocation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_invocation, Unset):
            last_invocation = self.last_invocation.to_dict()

        query_template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query_template, Unset):
            query_template = self.query_template.to_dict()

        response: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response, Unset):
            response = self.response.to_dict()

        secret_headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.secret_headers, Unset):
            secret_headers = self.secret_headers.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "args_schema": args_schema,
                "class": class_,
                "created_at": created_at,
                "description": description,
                "id": id,
                "kind": kind,
                "method": method,
                "name": name,
                "revision": revision,
                "status": status,
                "timeout_ms": timeout_ms,
                "title": title,
                "updated_at": updated_at,
                "url": url,
                "used_by": used_by,
                "write": write,
            }
        )
        if body_template is not UNSET:
            field_dict["body_template"] = body_template
        if bound is not UNSET:
            field_dict["bound"] = bound
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_by_api_key_id is not UNSET:
            field_dict["created_by_api_key_id"] = created_by_api_key_id
        if created_by_name is not UNSET:
            field_dict["created_by_name"] = created_by_name
        if fallback_line is not UNSET:
            field_dict["fallback_line"] = fallback_line
        if headers is not UNSET:
            field_dict["headers"] = headers
        if last_invocation is not UNSET:
            field_dict["last_invocation"] = last_invocation
        if query_template is not UNSET:
            field_dict["query_template"] = query_template
        if response is not UNSET:
            field_dict["response"] = response
        if secret_headers is not UNSET:
            field_dict["secret_headers"] = secret_headers

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.tool_invocation_summary import ToolInvocationSummary
        from ..models.tool_response_handling import ToolResponseHandling
        from ..models.tool_use import ToolUse
        from ..models.workspace_tool_args_schema import WorkspaceToolArgsSchema
        from ..models.workspace_tool_body_template import WorkspaceToolBodyTemplate
        from ..models.workspace_tool_bound import WorkspaceToolBound
        from ..models.workspace_tool_headers import WorkspaceToolHeaders
        from ..models.workspace_tool_query_template import WorkspaceToolQueryTemplate
        from ..models.workspace_tool_secret_headers import WorkspaceToolSecretHeaders

        d = dict(src_dict)
        args_schema = WorkspaceToolArgsSchema.from_dict(d.pop("args_schema"))

        class_ = check_workspace_tool_class(d.pop("class"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        description = d.pop("description")

        id = UUID(d.pop("id"))

        kind = check_workspace_tool_kind(d.pop("kind"))

        method = check_workspace_tool_method(d.pop("method"))

        name = d.pop("name")

        revision = d.pop("revision")

        status = check_workspace_tool_status(d.pop("status"))

        timeout_ms = d.pop("timeout_ms")

        title = d.pop("title")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        url = d.pop("url")

        used_by = []
        _used_by = d.pop("used_by")
        for used_by_item_data in _used_by:
            used_by_item = ToolUse.from_dict(used_by_item_data)

            used_by.append(used_by_item)

        write = d.pop("write")

        _body_template = d.pop("body_template", UNSET)
        body_template: WorkspaceToolBodyTemplate | Unset
        if isinstance(_body_template, Unset):
            body_template = UNSET
        else:
            body_template = WorkspaceToolBodyTemplate.from_dict(_body_template)

        _bound = d.pop("bound", UNSET)
        bound: WorkspaceToolBound | Unset
        if isinstance(_bound, Unset):
            bound = UNSET
        else:
            bound = WorkspaceToolBound.from_dict(_bound)

        _created_by = d.pop("created_by", UNSET)
        created_by: UUID | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = UUID(_created_by)

        _created_by_api_key_id = d.pop("created_by_api_key_id", UNSET)
        created_by_api_key_id: UUID | Unset
        if isinstance(_created_by_api_key_id, Unset):
            created_by_api_key_id = UNSET
        else:
            created_by_api_key_id = UUID(_created_by_api_key_id)

        created_by_name = d.pop("created_by_name", UNSET)

        fallback_line = d.pop("fallback_line", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: WorkspaceToolHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = WorkspaceToolHeaders.from_dict(_headers)

        _last_invocation = d.pop("last_invocation", UNSET)
        last_invocation: ToolInvocationSummary | Unset
        if isinstance(_last_invocation, Unset):
            last_invocation = UNSET
        else:
            last_invocation = ToolInvocationSummary.from_dict(_last_invocation)

        _query_template = d.pop("query_template", UNSET)
        query_template: WorkspaceToolQueryTemplate | Unset
        if isinstance(_query_template, Unset):
            query_template = UNSET
        else:
            query_template = WorkspaceToolQueryTemplate.from_dict(_query_template)

        _response = d.pop("response", UNSET)
        response: ToolResponseHandling | Unset
        if isinstance(_response, Unset):
            response = UNSET
        else:
            response = ToolResponseHandling.from_dict(_response)

        _secret_headers = d.pop("secret_headers", UNSET)
        secret_headers: WorkspaceToolSecretHeaders | Unset
        if isinstance(_secret_headers, Unset):
            secret_headers = UNSET
        else:
            secret_headers = WorkspaceToolSecretHeaders.from_dict(_secret_headers)

        workspace_tool = cls(
            args_schema=args_schema,
            class_=class_,
            created_at=created_at,
            description=description,
            id=id,
            kind=kind,
            method=method,
            name=name,
            revision=revision,
            status=status,
            timeout_ms=timeout_ms,
            title=title,
            updated_at=updated_at,
            url=url,
            used_by=used_by,
            write=write,
            body_template=body_template,
            bound=bound,
            created_by=created_by,
            created_by_api_key_id=created_by_api_key_id,
            created_by_name=created_by_name,
            fallback_line=fallback_line,
            headers=headers,
            last_invocation=last_invocation,
            query_template=query_template,
            response=response,
            secret_headers=secret_headers,
        )

        return workspace_tool
