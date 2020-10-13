import unittest

from io import StringIO
from unittest.mock import patch

from toy_robot_simulator import Simulator
from toy_robot_cli import main


class TestCLI(unittest.TestCase):
    def setUp(self):
        self.sim = Simulator

    def test_cli(self):

        def assert_stdin_stdout_equal(stdin_filename, stdout_filename):
            """
            helper function to mock stdin and stdout with test files
            and ensure stdin and stdout is equal
            """
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                main(input_filename=stdin_filename)
                with open(stdout_filename) as out:
                    expected_out = "".join(out.readlines())
                    self.assertEqual(mock_stdout.getvalue(), expected_out)

        assert_stdin_stdout_equal(
            "test/test_input01.txt", "test/test_output01.txt")
        assert_stdin_stdout_equal(
            "test/test_input02.txt", "test/test_output02.txt")
        assert_stdin_stdout_equal(
            "test/test_input03.txt", "test/test_output03.txt")


if __name__ == '__main__':
    unittest.main()
