from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain import LLMMathChain
import requests
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_github_commits():
    repo = os.getenv("GITHUB_REPO_NAME")
    owner = os.getenv("GITHUB_OWNER")
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    headers = {
        'Authorization': f'token {os.getenv("GITHUB_API_TOKEN")}',
        'Accept': 'application/vnd.github+json'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        commits = [commit['commit']['message'] for commit in data]
        return commits
    else:
        return f"Error: {response.status_code}, {response.text}"

class GithubCommitsTool(Tool):
    def __init__(self):
        super().__init__(
            name="GitHub Commits",
            func=self.fetch_commits,
            description="Fetches all commits from a given GitHub repository"
        )

    def fetch_commits(self, query: str) -> str:
        commits = fetch_github_commits()
        return '\n'.join(commits)

tools = [GithubCommitsTool()]
llm = OpenAI(temperature=0)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

response = agent.run(f"Get commits for the '{os.getenv('GITHUB_REPO_NAME')}' repository owned by '{os.getenv('GITHUB_OWNER')}'")
print(response)
