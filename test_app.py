import unittest
import requests
from unittest.mock import patch
from app import get_joke


class TestJokeApp(unittest.TestCase):

    @patch("app.requests.get")
    def test_get_joke_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "setup": "Why did the student bring a ladder?",
            "punchline": "Because they wanted to go to high school!"
        }

        result = get_joke()
        self.assertIsNotNone(result)
        self.assertIn("setup", result)
        self.assertIn("punchline", result)

    @patch("app.requests.get")
    def test_get_joke_failure(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Connection failed")

        result = get_joke()
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()