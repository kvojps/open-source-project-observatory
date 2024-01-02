from pydantic import BaseModel
from typing import Optional


class IssueGraphicResponse(BaseModel):
    open_issues: Optional[int]
    closed_issues: Optional[int]


class LabelIssueResponse(BaseModel):
    name: Optional[str]
    total: Optional[int]


class PullRequestGraphicResponse(BaseModel):
    open_pull_requests: Optional[int]
    closed_pull_requests: Optional[int]
    merged_pull_requests: Optional[int]
