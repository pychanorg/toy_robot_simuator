import unittest

from toy_robot_simulator import Table


class TestTable(unittest.TestCase):
    def setUp(self):
        self.table = Table()

    def test_square_table(self):
        self.table.init_square_table(0)
        self.assertEqual(self.table.valid_coordinates, [])
        self.assertFalse(self.table.is_valid_coordinate(0, 0))

        self.table.init_square_table(1)
        expected = [(0, 0)]
        self.assertEqual(self.table.valid_coordinates, expected)
        self.assertTrue(self.table.is_valid_coordinate(0, 0))
        self.assertFalse(self.table.is_valid_coordinate(0, 1))

        self.table.init_square_table(5)
        self.assertTrue(self.table.is_valid_coordinate(0, 0))
        self.assertTrue(self.table.is_valid_coordinate(0, 1))
        self.assertTrue(self.table.is_valid_coordinate(4, 4))

        self.assertFalse(self.table.is_valid_coordinate(-1, -1))
        self.assertFalse(self.table.is_valid_coordinate(4, 5))


if __name__ == '__main__':
    unittest.main()
