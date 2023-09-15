
from typing import List
from .data_analysis import AnalysisResult
from .github_api import RepoData

class ResponseGenerator:
    def __init__(self):
        pass

class Response:
    def __init__(self, description: str, relevance: str, additional_info: str):
        self.description = description
        self.relevance = relevance
        self.additional_info = additional_info

def generate_response(analysis_results: List[AnalysisResult], prompt: str) -> List[Response]:
    responses = []
    for result in analysis_results:
        description = f"Repo {result.repo_name} is a {result.repo_type} repository."
        relevance = f"This repo is relevant to your prompt '{prompt}' because it contains {result.keyword_matches} keyword matches."
        additional_info = f"Additional Info: {result.additional_info}"
        response = Response(description, relevance, additional_info)
        responses.append(response)
    return responses