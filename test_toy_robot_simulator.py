import unittest

from toy_robot_simulator import Table, Direction, Movement, Robot, Simulator


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


class TestDirection(unittest.TestCase):
    def test_is_valid_direction(self):
        self.assertTrue(Direction.is_valid_direction("NORTH"))
        self.assertTrue(Direction.is_valid_direction("SOUTH"))
        self.assertTrue(Direction.is_valid_direction("EAST"))
        self.assertTrue(Direction.is_valid_direction("WEST"))

        # test for lower cases and mixed cases and extra spacing
        self.assertTrue(Direction.is_valid_direction("WEST "))
        self.assertTrue(Direction.is_valid_direction(" WEST "))
        self.assertTrue(Direction.is_valid_direction(" west "))

        # test for invalid cases
        self.assertFalse(Direction.is_valid_direction(""))
        self.assertFalse(Direction.is_valid_direction("YES"))

    def test_rotation_left(self):
        self.assertEqual(Direction.rotate_left("NORTH"), "WEST")
        self.assertEqual(Direction.rotate_left("north "), "WEST")

    def test_rotation_right(self):
        self.assertEqual(Direction.rotate_right("north "), "EAST")
        self.assertEqual(Direction.rotate_right("south"), "WEST")

        self.assertNotEqual(Direction.rotate_right("south"), "WeST")


class TestMovement(unittest.TestCase):
    def test_forward(self):
        actual = Movement.forward(1, "NORTH", (0, 0))
        self.assertEqual(actual, (0, 1))

        actual = Movement.forward(1, "SOUTH", (0, 0))
        self.assertEqual(actual, (0, -1))

        actual = Movement.forward(1, "EAST", (0, 0))
        self.assertEqual(actual, (1, 0))

        actual = Movement.forward(1, "WEST", (0, 0))
        self.assertEqual(actual, (-1, 0))


class TestRobot(unittest.TestCase):
    def setUp(self):
        self.robot = Robot()

    def test_uninitialized_robot(self):
        # test uninitialized robot
        self.assertFalse(self.robot.is_initialized)
        self.assertFalse(self.robot.move())
        self.assertFalse(self.robot.left())
        self.assertFalse(self.robot.right())

        self.assertEqual(str(self.robot), "")

    def test_initialize_robot(self):
        self.robot.place(1, 2, 'NORTH')
        self.assertEqual(self.robot.x, 1)
        self.assertEqual(self.robot.y, 2)
        self.assertEqual(self.robot.direction, 'NORTH')
        self.assertTrue(self.robot.is_initialized)
        self.assertEqual(str(self.robot), "1 2 NORTH")

        self.assertTrue(self.robot.move())
        self.assertTrue(self.robot.left())
        self.assertTrue(self.robot.right())

    def test_move(self):
        pass

    def test_rotation(self):
        self.robot.place(1, 2, 'NORTH')
        # complete a full left rotation
        self.assertTrue(self.robot.left())
        self.assertTrue(self.robot.direction, 'WEST')
        self.assertTrue(self.robot.left())
        self.assertTrue(self.robot.direction, 'SOUTH')
        self.assertTrue(self.robot.left())
        self.assertTrue(self.robot.direction, 'EAST')
        self.assertTrue(self.robot.left())
        self.assertTrue(self.robot.direction, 'NORTH')

        # complete a full right rotation
        self.assertTrue(self.robot.right())
        self.assertTrue(self.robot.direction, 'EAST')
        self.assertTrue(self.robot.right())
        self.assertTrue(self.robot.direction, 'SOUTH')
        self.assertTrue(self.robot.right())
        self.assertTrue(self.robot.direction, 'WEST')
        self.assertTrue(self.robot.right())
        self.assertTrue(self.robot.direction, 'NORTH')



if __name__ == '__main__':
    unittest.main()
