from typing import Any, Dict

import requests  # type: ignore
from fastapi import HTTPException, status
from requests import Response

from api.config.dynaconf import settings


class RepositoryClient:
    def __init__(self):
        ...

    @staticmethod
    def get_repository(owner: str, repo_name: str) -> Dict[str, Any]:
        url: str = "https://api.github.com/graphql"

        headers: Dict[str, str] = {
            "Authorization": f"Bearer {settings.GITHUB_TOKEN}",
            "Content-Type": "application/json",
        }

        query: str = f"""
        query {{
          repository(owner: "{owner}", name: "{repo_name}") {{
            description
            defaultBranchRef {{
              target {{
                ... on Commit {{
                  history(first:1) {{
                    edges {{
                      node {{
                        committedDate
                      }}
                    }}
                  }}
                  totalCommits: history {{
                    totalCount
                  }}
                }}
              }}
            }}
            homepageUrl
            repositoryTopics(first:5) {{
              edges {{
                node {{
                  topic {{
                    name
                  }}
                }}
              }}
            }}
            stargazers {{
              totalCount
            }}
            mentionableUsers(first:1) {{
              totalCount
            }}
            forks {{
              totalCount
            }}
            refs(refPrefix: "refs/heads/") {{
              totalCount
            }}
            issues {{
              totalCount
            }}
            openIssues: issues(states: OPEN) {{
              totalCount
            }}
            closedIssues: issues(states: CLOSED) {{
              totalCount
            }}
            labels(first:100) {{
              nodes {{
                name
                  issues {{
                    totalCount
                  }}
              }}
            }}
            pullRequests {{
              totalCount
            }}
            openPullRequests: pullRequests(states: OPEN) {{
              totalCount
            }}
            closedPullRequests: pullRequests(states: CLOSED) {{
              totalCount
            }}
            mergedPullRequests: pullRequests(states: MERGED) {{
              totalCount
            }}
          }}
        }}
        """

        response: Response = requests.post(url, headers=headers, json={"query": query})
        if 200 >= response.status_code > 300:
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY, detail="Github API unavailable"
            )

        return response.json()
