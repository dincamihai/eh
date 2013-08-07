import unittest
import json
from mock import Mock, patch, call

from elasticapi import eh

MOCK_SERVERS_INFO = [
  {
    "block:0": "cb3d8f25",
    "name": "scala",
    "server": "cf299f87"
  },
  {
    "block:0": "39f1c214",
    "block:1": "0f6155a5",
    "name": "ruby",
    "server": "d4daadad"
  },
  {
    "block:0": "b3370ebd",
    "name": "python",
    "server": "b58e6f40"
  }
]

MOCK_DRIVE_INFO = {
    "drive": "39f1c214",
    "name": "ruby"
}

class ApiTestCase(unittest.TestCase):

    @patch.object(eh, 'requests')
    def test_request_params(self, mock_requests):
        eh.servers_info()

        self.assertEqual(
            call.get(
                'https://api-lon-b.elastichosts.com/servers/info',
                auth=(eh.USER, eh.SECRET_KEY),
                headers={'Accept': 'application/json'}
             ),
            mock_requests.mock_calls[0])

    @patch.object(eh, 'requests')
    def test_drives_for_servers(self, mock_requests):
        mock_requests.get.side_effect = [
            Mock(text='{"name": "scala"}', status_code=200),
            Mock(text='{"name": "ruby"}', status_code=200),
            Mock(text='{"name": "drive1"}', status_code=200),
            Mock(text='{"name": "python"}', status_code=200)]

        self.assertEqual(
            {'scala' : ['scala'],
             'ruby'  : ['ruby', 'drive1'],
             'python': ['python']},
            eh.drives_for_servers(MOCK_SERVERS_INFO))

    @patch.object(eh, 'requests')
    def test_drive_name(self, mock_requests):
        response_mock = Mock(text=json.dumps(MOCK_DRIVE_INFO), status_code=200)
        mock_requests.get = Mock(return_value=response_mock)
        self.assertEqual('ruby', eh.drive_name('39f1c214'))
