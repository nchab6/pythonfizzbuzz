import unittest
from main import main
from io import StringIO
import sys

class TestMain(unittest.TestCase):
    def test_main_output(self):
        # Redirect stdout to capture print output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the main function
        main()

        # Reset redirect
        sys.stdout = sys.__stdout__

        # Check if the output is as expected
        self.assertEqual(captured_output.getvalue().strip(), "Hello world")

if __name__ == '__main__':
    unittest.main()
