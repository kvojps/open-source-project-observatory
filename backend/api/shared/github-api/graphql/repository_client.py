import requests
from api.config.dynaconf import settings


class RepositoryClient:
    def __init__(self):
        ...

    @staticmethod
    def get_repository(owner: str, repo_name: str) -> requests.Response:
        url = 'https://api.github.com/graphql'

        headers = {
            'Authorization': f'Bearer {settings.GITHUB_TOKEN}',
            'Content-Type': 'application/json',
        }

        query = f'''
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
        '''

        response = requests.post(url, headers=headers, json={'query': query})

        return response.json()