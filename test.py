import unittest
from xml_to_json import to_json


class to_json_test(unittest.TestCase):

    def test_one(self):
        # Testing with an existing xml file should return true
        obj = to_json('hidden.screening').convert()
        self.assertTrue(obj)

    def test_two(self):
        # Testing with a files that does not exist should return a
        # File does not exist string
        obj = to_json('donor').convert()
        assert obj == "File does not exist"

    def test_tree(self):
        # Testing with an existing xml file, but that contains the wrong format
        obj = to_json('donor.disqualified').convert()
        assert obj == "xml file format is invalid"

if __name__ == '__main__':
    unittest.main()
