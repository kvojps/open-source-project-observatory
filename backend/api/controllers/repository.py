from fastapi import APIRouter, Path

from api.services.dtos.repository import RepositoryResponse
from api.services.repository import RepositoryService

router = APIRouter()


@router.get("/{owner}/{repo_name}", response_model=RepositoryResponse)
def get_repository(owner: str = Path(..., title="Owner of the repository"),
                   repo_name: str = Path(..., title="Name of the repository")):
    return RepositoryService.get_repository(owner=owner, repo_name=repo_name)
