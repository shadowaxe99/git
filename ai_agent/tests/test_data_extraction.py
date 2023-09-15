```python
import unittest
from ai_agent.data_extraction import extract_data

class TestDataExtraction(unittest.TestCase):

    def setUp(self):
        self.repo_url = "https://github.com/example/repo"
        self.expected_data = {
            'description': 'This is an example repo',
            'file_names': ['file1.py', 'file2.py'],
            'file_contents': ['print("Hello, world!")', 'print("Goodbye, world!")']
        }

    def test_extract_data(self):
        result = extract_data(self.repo_url)
        self.assertEqual(result, self.expected_data)

if __name__ == '__main__':
    unittest.main()
```