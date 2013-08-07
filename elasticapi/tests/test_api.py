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

MOCK_DRIVES_INFO = [
  {
    "drive": "39f1c214",
    "name": "ruby"
  },
  {
    "drive": "b3370ebd",
    "name": "python"
  },
  {
    "drive": "cb3d8f25",
    "name": "scala",
  },
  {
    "drive": "0f6155a5",
    "name": "drive1"
  }
]

class ApiTestCase(unittest.TestCase):

    @patch.object(eh, 'requests')
    def test_request_params(self, mock_requests):
        eh.servers_info()

        self.assertEqual(
            call.get(
                'https://api-lon-b.elastichosts.com/drives/info',
                auth=(eh.USER, eh.SECRET_KEY),
                headers={'Accept': 'application/json'}
             ),
            mock_requests.mock_calls[0])

        self.assertEqual(
            call.get(
                'https://api-lon-b.elastichosts.com/servers/info',
                auth=(eh.USER, eh.SECRET_KEY),
                headers={'Accept': 'application/json'}
             ),
            mock_requests.mock_calls[1])

    @patch.object(eh, 'requests')
    def test_drives_for_servers(self, mock_requests):
        output = eh.drives_for_servers(MOCK_SERVERS_INFO, MOCK_DRIVES_INFO)
        assert len(mock_requests.get.mock_calls) == 0, 'no requests needed'
        self.assertEqual(
            {'scala' : ['scala'],
             'ruby'  : ['ruby', 'drive1'],
             'python': ['python']},
            output)
