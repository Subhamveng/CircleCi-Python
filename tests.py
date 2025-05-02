import unittest
from main import to_lower

class MyTestCase(unittest.TestCase):
    def test_to_lower(self):
        name = "SubhamPradhan"
        lower_name = to_lower(name)
        self.assertEqual(lower_name, "subhampradhan")

if __name__ == '__main__':
    unittest.main()

#done
