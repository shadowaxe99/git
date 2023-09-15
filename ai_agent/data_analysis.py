import nltk
from collections import Counter
from ai_agent.data_extraction import RepoData


class DataAnalyzer:
    def __init__(self, repo_description, file_names, file_contents, topic):
        '''
        Initialize the DataAnalyzer class.

        Args:
            repo_description (str): The description of the repository.
            file_names (List[str]): The names of the files in the repository.
            file_contents (List[str]): The contents of the files in the repository.
            topic (str): The identified topic of the repository.
        '''
        self.repo_description = repo_description
        self.file_names = file_names
        self.file_contents = file_contents
        self.topic = topic


def analyze_data(repo_data):
    '''
    Analyze the repository data and identify the most common topic.

    Args:
        repo_data (RepoData): The repository data to analyze.

    Returns:
        AnalysisResult: The analysis result containing the frequency counts and the identified topic.
    '''
    # Analyze repo description
    repo_description = nltk.word_tokenize(repo_data.repo_description)
    repo_description_freq = Counter(repo_description)

    # Analyze file names
    file_names = nltk.word_tokenize(' '.join(repo_data.file_names))
    file_names_freq = Counter(file_names)

    # Analyze file contents
    file_contents = nltk.word_tokenize(' '.join(repo_data.file_contents))
    file_contents_freq = Counter(file_contents)

    # Identify the topic
    topic = identify_topic(repo_description_freq, file_names_freq, file_contents_freq)

    return AnalysisResult(repo_description_freq, file_names_freq, file_contents_freq, topic)


def identify_topic(repo_description_freq, file_names_freq, file_contents_freq):
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