Shared Dependencies:

1. Variables:
   - `github_api_key`: The API key for accessing GitHub API.
   - `monitor_keywords`: List of keywords to monitor on GitHub.

2. Data Schemas:
   - `RepoData`: Schema for the data extracted from GitHub repos, including repo description, file names, and file contents.
   - `AnalysisResult`: Schema for the result of data analysis, including what the repos do and how they work.
   - `Response`: Schema for the generated response, including the description of the repos, their relevance to the prompt, and any other relevant information.

3. Function Names:
   - `identify_topic()`: Function to identify the topic of the prompt.
   - `find_repos()`: Function to find relevant GitHub repos.
   - `extract_data()`: Function to extract data from the repos.
   - `analyze_data()`: Function to analyze the extracted data.
   - `generate_response()`: Function to generate a response based on the analysis.
   - `monitor_github()`: Function to continuously monitor GitHub for certain keywords.

4. Message Names:
   - `NewRepoNotification`: Message sent when a new relevant repo is found.
   - `RepoRecommendation`: Message sent with recommendations for relevant GitHub repos.
   - `TrendReport`: Message sent with a report on the latest trends in GitHub repos.

5. Configurations:
   - `config.py`: Contains shared configurations like API keys, monitoring frequency, etc.

6. Test Functions:
   - `test_identify_topic()`
   - `test_find_repos()`
   - `test_extract_data()`
   - `test_analyze_data()`
   - `test_generate_response()`
   - `test_monitor_github()`