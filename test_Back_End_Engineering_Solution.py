import unittest
from unittest.mock import MagicMock
from Back_End_Engineering_Solution import main_request

class TestMainRequest(unittest.TestCase):
    def setUp(self):
        self.mock_response = MagicMock()
        self.mock_response.status_code = 200
        self.mock_response.json.return_value = {'message': 'Success'}
        self.mock_response.content = 'Mock Response Content'

    def test_successful_request(self):
        # Mock the requests library to return a successful response
        requests = MagicMock()
        requests.request.return_value = self.mock_response

        # Patch the requests library within the scope of the test
        with unittest.mock.patch('Back_End_Engineering_Solution.requests', requests):
            result = main_request("GET", "endpoint")

        self.assertEqual(result, {'message': 'Success'})

    def test_failed_request(self):
        # Mock the requests library to return a failed response
        failed_response = MagicMock()
        failed_response.status_code = 400
        failed_response.content = 'Mock Failed Response Content'
        requests = MagicMock()
        requests.request.return_value = failed_response

        # Patch the requests library within the scope of the test
        with unittest.mock.patch('Back_End_Engineering_Solution.requests', requests):
            with self.assertRaises(Exception) as cm:
                main_request("POST", "endpoint")

        self.assertEqual(str(cm.exception), "Request failed with status code 400")

if __name__ == '__main__':
    unittest.main()
