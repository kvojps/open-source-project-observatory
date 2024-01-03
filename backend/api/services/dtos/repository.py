from typing import List, Optional

from pydantic import BaseModel

from .repository_graphics import (IssueGraphicResponse, LabelResponse,
                                  PullRequestGraphicResponse)


class RepositoryResponse(BaseModel):
    owner: Optional[str]
    name: Optional[str]
    description: Optional[str]
    last_activity: Optional[str]
    license_url: Optional[str]
    website_url: Optional[str]
    topics: Optional[List[str]]
    stars_amount: Optional[int]
    readme_url: Optional[str]
    contribution_url: Optional[str]
    contributors_amount: Optional[int]
    forks_amount: Optional[int]
    branches_amount: Optional[int]
    issues_amount: Optional[int]
    prs_amount: Optional[int]
    commits_amount: Optional[int]
    issues_graphic: Optional[IssueGraphicResponse]
    prs_graphic: Optional[PullRequestGraphicResponse]
    top_ten_labels_graphic: Optional[List[LabelResponse]]

    @classmethod
    def from_repository_response(cls, owner: str, name: str, repository_data) -> "RepositoryResponse":
        labels_data = repository_data.get("labels", None).get("nodes", None)
        sorted_labels_data = sorted(
            labels_data, key=lambda x: x["issues"]["totalCount"], reverse=True)

        return cls(
            owner=owner,
            name=name,
            description=repository_data.get("description", None),
            last_activity=repository_data.get("defaultBranchRef", None).get("target", None).get("history", None).get(
                "edges", None)[0].get("node", None).get("committedDate", None),
            license_url=None,
            website_url=repository_data.get("homepageUrl", None),
            topics=[topic["node"]["topic"]["name"] for topic in
                    repository_data.get("repositoryTopics", None).get("edges", [])],
            stars_amount=repository_data.get(
                "stargazers", None).get("totalCount", None),
            readme_url=None,
            contribution_url=None,
            contributors_amount=repository_data.get(
                "mentionableUsers", None).get("totalCount", None),
            forks_amount=repository_data.get(
                "forks", None).get("totalCount", None),
            branches_amount=repository_data.get(
                "refs", None).get("totalCount", None),
            issues_amount=repository_data.get(
                "issues", None).get("totalCount", None),
            prs_amount=repository_data.get(
                "pullRequests", None).get("totalCount", None),
            commits_amount=repository_data.get("defaultBranchRef", None).get("target", None).get("totalCommits",
                                                                                                 None).get("totalCount",
                                                                                                           None),
            issues_graphic=IssueGraphicResponse(
                open_issues=repository_data.get(
                    "openIssues", None).get("totalCount", None),
                closed_issues=repository_data.get(
                    "closedIssues", None).get("totalCount", None)
            ),
            prs_graphic=PullRequestGraphicResponse(
                open_pull_requests=repository_data.get(
                    "openPullRequests", None).get("totalCount", None),
                closed_pull_requests=repository_data.get(
                    "closedPullRequests", None).get("totalCount", None),
                merged_pull_requests=repository_data.get(
                    "mergedPullRequests", None).get("totalCount", None)
            ),
            top_ten_labels_graphic=[
                LabelResponse(name=label["name"],
                              total=label["issues"]["totalCount"])
                for label in sorted_labels_data[:10]
            ]
        )
