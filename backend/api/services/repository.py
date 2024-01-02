from api.shared.github_api.graphql.repository_client import RepositoryClient
from .dtos.repository import RepositoryResponse


class RepositoryService:
    def __init__(self):
        ...

    @staticmethod
    def get_repository(owner: str, repo_name: str) -> RepositoryResponse:
        repository_json = RepositoryClient.get_repository(owner, repo_name)
        return RepositoryResponse.from_repository_response(owner, repo_name, repository_json)
