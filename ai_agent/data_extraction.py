
import requests
from typing import Dict, List
from .github_api import GithubAPI
from .config import github_api_key

class RepoData:
    def __init__(self, description: str, file_names: List[str], file_contents: List[str]):
        self.description = description
        self.file_names = file_names
        self.file_contents = file_contents

class DataExtractor:
    def __init__(self):
        self.github_api = GithubAPI(github_api_key)

    def extract_data(self, repo_url: str) -> RepoData:
        repo_info = self.github_api.get_repo_info(repo_url)
        description = repo_info['description']
        file_names, file_contents = self._get_files_data(repo_info['contents_url'])
        return RepoData(description, file_names, file_contents)

    def _get_files_data(self, contents_url: str) -> (List[str], List[str]):
        files_info = self.github_api.get_files_info(contents_url)
        file_names = [file_info['name'] for file_info in files_info]
        file_contents = [self._get_file_content(file_info['download_url']) for file_info in files_info]
        return file_names, file_contents

    def _get_file_content(self, download_url: str) -> str:
        response = requests.get(download_url)
        response.raise_for_status()
        return response.text