from .github_api import GithubAPI
from .data_extraction import DataExtractor
from .data_analysis import DataAnalyzer
from .response_generation import ResponseGenerator
from .monitoring import GithubMonitor
from .utils import identify_topic

class AIAgent:
    def __init__(self, github_api_key, monitor_keywords):
        self.github_api = GithubAPI(github_api_key)
        self.data_extractor = DataExtractor()
        self.data_analyzer = DataAnalyzer()
        self.response_generator = ResponseGenerator()
        self.monitor = GithubMonitor(github_api_key, monitor_keywords)

    def process_prompt(self, prompt):
        topic = identify_topic(prompt)
        repos = self.github_api.find_repos(topic)
        repo_data = [self.data_extractor.extract_data(repo) for repo in repos]
        analysis_results = [self.data_analyzer.analyze_data(data) for data in repo_data]
        responses = [self.response_generator.generate_response(result) for result in analysis_results]
        return responses

    def start_monitoring(self):
        self.monitor.start_monitoring(self.process_prompt)