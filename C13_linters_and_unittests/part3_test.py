import json
import unittest
from unittest.mock import patch, MagicMock

from C13_linters_and_unittests.part3 import time_getter

output = ['Africa/Abidjan', 'Africa/Accra']


class TestTimeGetter(unittest.TestCase):
    @patch("C13_linters_and_unittests.part3.requests.get")
    def test_content(self, get_mock):
        get_mock.return_value = MagicMock(text=json.dumps(output))
        self.assertEqual(time_getter(), output)


if __name__ == '__main__':
    unittest.main()
