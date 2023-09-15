import requests
from typing import List, Dict
from .config import github_api_key

class GithubAPI:
    def __init__(self, github_api_key):
        self.github_api_key = github_api_key

BASE_URL = "https://api.github.com"

def find_repos(topic: str) -> List[Dict]:
    headers = {"Authorization": f"token {github_api_key}"}
    response = requests.get(f"{BASE_URL}/search/repositories?q={topic}+in:readme", headers=headers)
    response.raise_for_status()
    return response.json()["items"]

def extract_data(repo_url: str) -> Dict:
    headers = {"Authorization": f"token {github_api_key}"}
    response = requests.get(f"{repo_url}", headers=headers)
    response.raise_for_status()
    return response.json()

def monitor_github(keywords: List[str]) -> List[Dict]:
    headers = {"Authorization": f"token {github_api_key}"}
    results = []
    for keyword in keywords:
        response = requests.get(f"{BASE_URL}/search/repositories?q={keyword}+in:readme", headers=headers)
        response.raise_for_status()
        results.extend(response.json()["items"])
    return results