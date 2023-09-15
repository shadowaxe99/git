import nltk
from collections import Counter
from ai_agent.data_extraction import RepoData


class RepoAnalyzer:
    def __init__(self, repo_data):
        '''
        Initialize the RepoAnalyzer class.

        Args:
            repo_data (RepoData): The repository data to analyze.
        '''
        self.repo_data = repo_data

    def analyze_repo(self):
        '''
        Analyze the repository data and identify the most common topic.

        Returns:
            AnalysisResult: The analysis result containing the frequency counts and the identified topic.
        '''
        # Analyze repo description
        repo_description = nltk.word_tokenize(self.repo_data.repo_description)
        repo_description_freq = Counter(repo_description)

        # Analyze file names
        file_names = nltk.word_tokenize(' '.join(self.repo_data.file_names))
        file_names_freq = Counter(file_names)

        # Analyze file contents
        file_contents = nltk.word_tokenize(' '.join(self.repo_data.file_contents))
        file_contents_freq = Counter(file_contents)

        # Identify the topic
        topic = self.identify_topic(repo_description_freq, file_names_freq, file_contents_freq)

        return AnalysisResult(repo_description_freq, file_names_freq, file_contents_freq, topic)

    def identify_topic(self, repo_description_freq, file_names_freq, file_contents_freq):
        '''
        Identify the most common topic based on the frequency counts.

        Args:
            repo_description_freq (Counter): The frequency counts of words in the repository description.
            file_names_freq (Counter): The frequency counts of words in the file names.
            file_contents_freq (Counter): The frequency counts of words in the file contents.

        Returns:
            str: The identified topic.
        '''
        # Combine all frequencies
        combined_freq = repo_description_freq + file_names_freq + file_contents_freq

        # Identify the most common topic
        topic = combined_freq.most_common(1)[0][0]

        return topic