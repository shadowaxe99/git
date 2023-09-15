```python
import unittest
from ai_agent.data_analysis import analyze_data

class TestDataAnalysis(unittest.TestCase):

    def setUp(self):
        self.sample_data = {
            "description": "A sample GitHub repo for testing",
            "file_names": ["main.py", "utils.py", "README.md"],
            "file_contents": ["print('Hello, World!')", "def add(a, b): return a + b", "# This is a sample repo"]
        }

    def test_analyze_data(self):
        result = analyze_data(self.sample_data)
        self.assertIsInstance(result, dict)
        self.assertIn('repo_purpose', result)
        self.assertIn('repo_working', result)

if __name__ == '__main__':
    unittest.main()
```