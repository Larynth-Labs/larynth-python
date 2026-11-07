from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.workspace_tool_input_class import (
    WorkspaceToolInputClass,
    check_workspace_tool_input_class,
)
from ..models.workspace_tool_input_method import (
    WorkspaceToolInputMethod,
    check_workspace_tool_input_method,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_response_handling import ToolResponseHandling
    from ..models.workspace_tool_input_args_schema import WorkspaceToolInputArgsSchema
    from ..models.workspace_tool_input_body_template import (
        WorkspaceToolInputBodyTemplate,
    )
    from ..models.workspace_tool_input_bound import WorkspaceToolInputBound
    from ..models.workspace_tool_input_headers import WorkspaceToolInputHeaders
    from ..models.workspace_tool_input_query_template import (
        WorkspaceToolInputQueryTemplate,
    )
    from ..models.workspace_tool_input_secret_headers import (
        WorkspaceToolInputSecretHeaders,
    )


T = TypeVar("T", bound="WorkspaceToolInput")


@_attrs_define
class WorkspaceToolInput:
    """
    Attributes:
        args_schema (WorkspaceToolInputArgsSchema): Closed object schema, at most 16 properties and depth 3
        class_ (WorkspaceToolInputClass): fast answers without a filler line; slow plays one filler first
        description (str): Shown to the model
        method (WorkspaceToolInputMethod):
        name (str): Name the model calls
        timeout_ms (int): fast 300 to 1500, slow 500 to 10000
        title (str):
        url (str): https only, no user info; checked against private and reserved addresses
        write (bool): Changes data: never retried
        body_template (WorkspaceToolInputBodyTemplate | Unset): JSON body with {{arg}} and {{call.field}} placeholders
        bound (WorkspaceToolInputBound | Unset): JSON pointer in the request to a call field the model cannot change:
            call_id, caller_e164, agent_e164, contact_id, campaign_id
        fallback_line (str | Unset): Spoken when the call fails
        headers (WorkspaceToolInputHeaders | Unset): Fixed headers; Authorization and Cookie need secret_headers
        query_template (WorkspaceToolInputQueryTemplate | Unset): Query parameters with {{arg}} and {{call.field}}
            placeholders
        response (ToolResponseHandling | Unset):
        secret_headers (WorkspaceToolInputSecretHeaders | Unset): Header name to secret id
    """

    args_schema: WorkspaceToolInputArgsSchema
    class_: WorkspaceToolInputClass
    description: str
    method: WorkspaceToolInputMethod
    name: str
    timeout_ms: int
    title: str
    url: str
    write: bool
    body_template: WorkspaceToolInputBodyTemplate | Unset = UNSET
    bound: WorkspaceToolInputBound | Unset = UNSET
    fallback_line: str | Unset = UNSET
    headers: WorkspaceToolInputHeaders | Unset = UNSET
    query_template: WorkspaceToolInputQueryTemplate | Unset = UNSET
    response: ToolResponseHandling | Unset = UNSET
    secret_headers: WorkspaceToolInputSecretHeaders | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        args_schema = self.args_schema.to_dict()

        class_: str = self.class_

        description = self.description

        method: str = self.method

        name = self.name

        timeout_ms = self.timeout_ms

        title = self.title

        url = self.url

        write = self.write

        body_template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.body_template, Unset):
            body_template = self.body_template.to_dict()

        bound: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bound, Unset):
            bound = self.bound.to_dict()

        fallback_line = self.fallback_line

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

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
                "description": description,
                "method": method,
                "name": name,
                "timeout_ms": timeout_ms,
                "title": title,
                "url": url,
                "write": write,
            }
        )
        if body_template is not UNSET:
            field_dict["body_template"] = body_template
        if bound is not UNSET:
            field_dict["bound"] = bound
        if fallback_line is not UNSET:
            field_dict["fallback_line"] = fallback_line
        if headers is not UNSET:
            field_dict["headers"] = headers
        if query_template is not UNSET:
            field_dict["query_template"] = query_template
        if response is not UNSET:
            field_dict["response"] = response
        if secret_headers is not UNSET:
            field_dict["secret_headers"] = secret_headers

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.tool_response_handling import ToolResponseHandling
        from ..models.workspace_tool_input_args_schema import (
            WorkspaceToolInputArgsSchema,
        )
        from ..models.workspace_tool_input_body_template import (
            WorkspaceToolInputBodyTemplate,
        )
        from ..models.workspace_tool_input_bound import WorkspaceToolInputBound
        from ..models.workspace_tool_input_headers import WorkspaceToolInputHeaders
        from ..models.workspace_tool_input_query_template import (
            WorkspaceToolInputQueryTemplate,
        )
        from ..models.workspace_tool_input_secret_headers import (
            WorkspaceToolInputSecretHeaders,
        )

        d = dict(src_dict)
        args_schema = WorkspaceToolInputArgsSchema.from_dict(d.pop("args_schema"))

        class_ = check_workspace_tool_input_class(d.pop("class"))

        description = d.pop("description")

        method = check_workspace_tool_input_method(d.pop("method"))

        name = d.pop("name")

        timeout_ms = d.pop("timeout_ms")

        title = d.pop("title")

        url = d.pop("url")

        write = d.pop("write")

        _body_template = d.pop("body_template", UNSET)
        body_template: WorkspaceToolInputBodyTemplate | Unset
        if isinstance(_body_template, Unset):
            body_template = UNSET
        else:
            body_template = WorkspaceToolInputBodyTemplate.from_dict(_body_template)

        _bound = d.pop("bound", UNSET)
        bound: WorkspaceToolInputBound | Unset
        if isinstance(_bound, Unset):
            bound = UNSET
        else:
            bound = WorkspaceToolInputBound.from_dict(_bound)

        fallback_line = d.pop("fallback_line", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: WorkspaceToolInputHeaders | Unset
        if isinstance(_headers, Unset):
            headers = UNSET
        else:
            headers = WorkspaceToolInputHeaders.from_dict(_headers)

        _query_template = d.pop("query_template", UNSET)
        query_template: WorkspaceToolInputQueryTemplate | Unset
        if isinstance(_query_template, Unset):
            query_template = UNSET
        else:
            query_template = WorkspaceToolInputQueryTemplate.from_dict(_query_template)

        _response = d.pop("response", UNSET)
        response: ToolResponseHandling | Unset
        if isinstance(_response, Unset):
            response = UNSET
        else:
            response = ToolResponseHandling.from_dict(_response)

        _secret_headers = d.pop("secret_headers", UNSET)
        secret_headers: WorkspaceToolInputSecretHeaders | Unset
        if isinstance(_secret_headers, Unset):
            secret_headers = UNSET
        else:
            secret_headers = WorkspaceToolInputSecretHeaders.from_dict(_secret_headers)

        workspace_tool_input = cls(
            args_schema=args_schema,
            class_=class_,
            description=description,
            method=method,
            name=name,
            timeout_ms=timeout_ms,
            title=title,
            url=url,
            write=write,
            body_template=body_template,
            bound=bound,
            fallback_line=fallback_line,
            headers=headers,
            query_template=query_template,
            response=response,
            secret_headers=secret_headers,
        )

        return workspace_tool_input
