```python
import time
from ai_agent import agent, config

def main():
    ai_agent = agent.AIAgent(config.github_api_key, config.monitor_keywords)

    while True:
        prompt = ai_agent.get_prompt()
        topic = ai_agent.identify_topic(prompt)
        relevant_repos = ai_agent.find_repos(topic)
        repo_data = ai_agent.extract_data(relevant_repos)
        analysis_result = ai_agent.analyze_data(repo_data)
        response = ai_agent.generate_response(analysis_result)
        ai_agent.send_response(response)
        ai_agent.monitor_github()
        time.sleep(config.monitoring_frequency)

if __name__ == "__main__":
    main()
```