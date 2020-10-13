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
        self.assertEqual(str(self.robot), "1,2,NORTH")

        self.assertTrue(self.robot.move())
        self.assertTrue(self.robot.left())
        self.assertTrue(self.robot.right())

    def test_move(self):
        self.robot.place(1, 2, 'NORTH')
        self.assertTrue(self.robot.move())
        self.assertEqual(self.robot.get_location(), (1, 3))
        self.assertTrue(self.robot.move())
        self.assertEqual(self.robot.get_location(), (1, 4))

        # rotate west and move
        self.assertTrue(self.robot.left())
        self.assertTrue(self.robot.move())
        self.assertEqual(self.robot.get_location(), (0, 4))

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


class TestSimulator(unittest.TestCase):
    def setUp(self):
        self.sim = Simulator()

    def test_uninitialized_moves(self):
        self.assertFalse(self.sim.move())
        self.assertFalse(self.sim.left())
        self.assertFalse(self.sim.right())
        self.assertEqual(self.sim.report(), "")

    def test_bad_initializations(self):
        self.assertFalse(self.sim.place(-1, -1, "WEST"))  # out of bounds
        self.assertFalse(self.sim.place(5, 4, "WEST"))  # out of bounds
        self.assertFalse(self.sim.place(4, 5, "WEST"))  # out of bounds

        self.assertFalse(self.sim.place(4, 4, "WES T"))  # bad direction

    def test_basic_moves(self):
        """
        Validate basic movements and assert correct functionally
        to avoid robot moving out of board
        """
        self.assertTrue(self.sim.place(1, 0, "WEST"))
        self.assertTrue(self.sim.move())
        self.assertEqual(self.sim.robot.get_location(), (0, 0))
        self.assertFalse(self.sim.move())  # assert invalid move
        self.assertEqual(self.sim.robot.get_location(), (0, 0))

        self.assertTrue(self.sim.place(3, 1, "EAST"))
        self.assertEqual(self.sim.robot.get_location(), (3, 1))
        self.assertTrue(self.sim.move())
        self.assertEqual(self.sim.robot.get_location(), (4, 1))
        self.assertFalse(self.sim.move())  # assert invalid move
        self.assertEqual(self.sim.robot.get_location(), (4, 1))


if __name__ == '__main__':
    unittest.main()
