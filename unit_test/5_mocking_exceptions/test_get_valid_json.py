import unittest
from unittest.mock import patch, Mock
from get_json import get_json


class TestGetJson(unittest.TestCase):
    def test_get_valid_json(self):
        with patch('builtins.open') as mock_open:
            # arrange
            filename = "does_not_exit.json"

            mock_file = Mock()
            mock_file.read.return_value = '{"foo":"bar"}'
            mock_open.return_value = mock_file

            # action
            actual_result = get_json(filename)

            # assert
            self.assertEqual({u'foo': u'bar'}, actual_result)


if __name__ == '__main__':
    unittest.main()
