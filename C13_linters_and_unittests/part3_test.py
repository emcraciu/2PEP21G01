import json
import unittest
from unittest.mock import patch, MagicMock

from C13_linters_and_unittests.part3 import time_getter
from part3 import my_func

output = ['Africa/Abidjan', 'Africa/Accra']


class TestTimeGetter(unittest.TestCase):
    @patch("C13_linters_and_unittests.part3.requests.get")
    def test_content(self, get_mock):
        get_mock.return_value = MagicMock(text=json.dumps(output))
        self.assertEqual(time_getter(), output)


class Example(unittest.TestCase):
    @patch("part3.json.loads")
    def test_func(self, my_mock):
        my_mock.return_value = {}
        self.assertEqual(my_func('{}'), {})


if __name__ == '__main__':
    unittest.main()
