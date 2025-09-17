import sys
import os
import unittest
from unittest.mock import Mock

# Add the project root to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

# Import azure functions
import azure.functions as func

# Import our function
from HttpTrigger import main


class TestHttpTrigger(unittest.TestCase):
    def test_post_request_returns_plop(self):
        # Create a mock POST request
        req = Mock(spec=func.HttpRequest)
        req.method = 'POST'
        
        # Call the function
        response = main(req)
        
        # Verify response
        self.assertEqual(response.get_body().decode('utf-8'), 'plop')
        self.assertEqual(response.status_code, 200)
    
    def test_non_post_request_returns_405(self):
        # Create a mock GET request
        req = Mock(spec=func.HttpRequest)
        req.method = 'GET'
        
        # Call the function
        response = main(req)
        
        # Verify response
        self.assertIn('only accepts POST requests', response.get_body().decode('utf-8'))
        self.assertEqual(response.status_code, 405)


if __name__ == '__main__':
    unittest.main()