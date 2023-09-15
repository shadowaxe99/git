```python
import time
from github_api import GithubAPI
from agent import Agent
from config import github_api_key, monitor_keywords

class Monitoring:
    def __init__(self):
        self.github_api = GithubAPI(github_api_key)
        self.agent = Agent()
        self.last_checked_repos = {}

    def monitor_github(self):
        while True:
            for keyword in monitor_keywords:
                repos = self.github_api.search_repos(keyword)
                for repo in repos:
                    if repo['id'] not in self.last_checked_repos:
                        self.last_checked_repos[repo['id']] = repo
                        repo_data = self.agent.extract_data(repo)
                        analysis_result = self.agent.analyze_data(repo_data)
                        response = self.agent.generate_response(analysis_result)
                        self.agent.send_message(response)
            time.sleep(60)  # Sleep for 60 seconds

if __name__ == "__main__":
    monitoring = Monitoring()
    monitoring.monitor_github()
```