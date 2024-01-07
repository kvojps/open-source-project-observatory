from typing import Any, Dict, Optional

from fastapi import HTTPException, status

from api.shared.github_api.graphql.repository_client import RepositoryClient

from .dtos.repository import RepositoryResponse


class RepositoryService:
    def __init__(self) -> None:
        ...

    @staticmethod
    def get_repository(owner: str, repo_name: str) -> RepositoryResponse:
        github_repo_response: Dict[str, Any] = RepositoryClient.get_repository(
            owner, repo_name)
        response_data: Optional[Dict[str, Any]
                                ] = github_repo_response.get("data", None)
        repository: Optional[Dict[str, Any]] = response_data.get(
            "repository", None) if response_data else None

        if not repository:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Repository not found")

        return RepositoryResponse.from_repository_response(owner, repo_name, repository)
