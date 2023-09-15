```python
import unittest
from unittest.mock import patch
from ai_agent.github_api import find_repos

class TestGithubAPI(unittest.TestCase):

    @patch('ai_agent.github_api.requests.get')
    def test_find_repos(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            'items': [
                {
                    'name': 'test_repo',
                    'description': 'This is a test repo',
                    'html_url': 'https://github.com/test/test_repo',
                    'contents_url': 'https://api.github.com/repos/test/test_repo/contents/{+path}'
                }
            ]
        }

        repos = find_repos('test')
        self.assertEqual(len(repos), 1)
        self.assertEqual(repos[0]['name'], 'test_repo')
        self.assertEqual(repos[0]['description'], 'This is a test repo')
        self.assertEqual(repos[0]['html_url'], 'https://github.com/test/test_repo')
        self.assertEqual(repos[0]['contents_url'], 'https://api.github.com/repos/test/test_repo/contents/{+path}')

if __name__ == '__main__':
    unittest.main()
```