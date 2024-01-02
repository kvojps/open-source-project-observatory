from fastapi import HTTPException, status
from api.shared.github_api.graphql.repository_client import RepositoryClient
from .dtos.repository import RepositoryResponse


class RepositoryService:
    def __init__(self):
        ...

    @staticmethod
    def get_repository(owner: str, repo_name: str) -> RepositoryResponse:
        repository_response_json = RepositoryClient.get_repository(owner, repo_name)
        if not repository_response_json.get("data").get("repository"):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Repository not found")

        return RepositoryResponse.from_repository_response(owner, repo_name, repository_response_json)
