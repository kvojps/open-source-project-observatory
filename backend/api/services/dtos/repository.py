from pydantic import BaseModel
from typing import List, Optional


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
    forks_amount: Optional[int]
    branches_amount: Optional[int]
    issues_amount: Optional[int]
    prs_amount: Optional[int]
    commits_amount: Optional[int]

    @classmethod
    def from_repository_response(cls, owner: str, name: str, github_response) -> "RepositoryResponse":
        repository_data = github_response.get("data", None).get("repository", None)

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
            stars_amount=repository_data.get("stargazers", None).get("totalCount"),
            readme_url=None,
            contribution_url=None,
            forks_amount=repository_data.get("forks", None).get("totalCount"),
            branches_amount=repository_data.get("refs", None).get("totalCount"),
            issues_amount=repository_data.get("issues", None).get("totalCount"),
            prs_amount=repository_data.get("pullRequests", None).get("totalCount"),
            commits_amount=repository_data.get("defaultBranchRef", None).get("target", None).get("totalCommits",
                                                                                                 None).get("totalCount",
                                                                                                           None)
        )
