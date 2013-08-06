import unittest
import json
from mock import Mock, patch, call

from elasticapi import eh

class ApiTestCase(unittest.TestCase):

    @patch.object(eh, 'requests')
    def test_request_params(self, mock_requests):
        eh.servers_info()

        mock_requests.get = Mock(return_value=json.dumps([
            'drive1', 'drive2'
        ]))
        self.assertEqual(
            [call.get(
                'https://api-lon-p.elastichosts.com/drives/list',
                auth=('dincamihai', 'SECRET_KEY')
             )],
            mock_requests.mock_calls)
