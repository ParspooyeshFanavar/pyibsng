import unittest
from ibsng.util import string


class TestUtil(unittest.TestCase):
    def test_connection_string_parser(self):
        r1 = string. \
            connection_string_parser("user:pass@http://192.168.1.1:8080")
        self.assertIsInstance(r1, tuple)
        self.assertEqual(r1[1], "http://192.168.1.1:8080")
        self.assertIsInstance(r1[0], dict)

        with self.assertRaises(Exception) as context:
            string.connection_string_parser("user:pass@192.168.1.1:8080")
        self.assertIn("Invalid connection string", str(context.exception))

        with self.assertRaises(Exception) as context:
            string.connection_string_parser("something wrong")
        self.assertIn("Invalid connection string", str(context.exception))

    def test_camel_to_snake(self):
        r1 = string.camel_to_snake("ibsngTest")
        self.assertEqual(r1, "ibsng_test")

        r1 = string.camel_to_snake("IbsngTest")
        self.assertEqual(r1, "ibsng_test")

        r1 = string.camel_to_snake("323232")
        self.assertEqual(r1, "323232")

        r1 = string.camel_to_snake("Ibsng_test")
        self.assertEqual(r1, "ibsng_test")
 
        r1 = string.camel_to_snake("_Ibsng_test")
        self.assertEqual(r1, "_ibsng_test")

if __name__ == "__main__":
    unittest.main()
