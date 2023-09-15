```python
import json
import requests

def load_config():
    with open('config.py', 'r') as f:
        config = json.load(f)
    return config

def send_request(url, headers):
    response = requests.get(url, headers=headers)
    return response.json()

def parse_repo_data(repo_data):
    return {
        'description': repo_data['description'],
        'file_names': [file['name'] for file in repo_data['files']],
        'file_contents': [file['content'] for file in repo_data['files']]
    }

def parse_analysis_result(analysis_result):
    return {
        'what_it_does': analysis_result['what_it_does'],
        'how_it_works': analysis_result['how_it_works']
    }

def parse_response(response):
    return {
        'description': response['description'],
        'relevance': response['relevance'],
        'other_info': response['other_info']
    }
```