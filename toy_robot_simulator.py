class Table:
    """
    Functions to help objects like robot in placement on a physical game board
    """

    def __init__(self):
        self.valid_coordinates = []

    def init_square_table(self, width):
        self.valid_coordinates = []
        for x in range(width):
            for y in range(width):
                self.valid_coordinates.append((x, y))

    def init_rectangle_table(self, width, height):
        self.valid_coordinates = []
        for x in range(width):
            for y in range(height):
                self.valid_coordinates.append((x, y))

    def is_valid_coordinate(self, x, y):
        try:
            # cooerce x/y to int
            # to handle cases where x/y are in strings
            x, y = int(x), int(y)
        except TypeError:
            pass
        if (x, y) in self.valid_coordinates:
            return True
        return False


class Direction:
    """
    Functions to assist objects like robots in direction and rotation
    """
    @classmethod
    def is_valid_direction(cls, direction):
        direction = direction.strip().upper()
        return direction in ["NORTH", "SOUTH", "EAST", "WEST"]

    @classmethod
    def rotate_left(cls, curr_direction):
        curr_direction = curr_direction.strip().upper()
        mapping = {
            "NORTH": "WEST",
            "EAST": "NORTH",
            "SOUTH": "EAST",
            "WEST": "SOUTH",
        }
        if curr_direction in mapping.keys():
            return mapping[curr_direction]
        return ""

    @classmethod
    def rotate_right(cls, curr_direction):
        curr_direction = curr_direction.strip().upper()
        mapping = {
            "NORTH": "EAST",
            "EAST": "SOUTH",
            "SOUTH": "WEST",
            "WEST": "NORTH",
        }
        if curr_direction in mapping.keys():
            return mapping[curr_direction]
        return ""


class Movement:
    """
    Functions to assist objects like robots in movement

    At the moment, only forward is implemented, but other possible movements
    like teleport, knockbacks, etc can be implemented
    """
    @classmethod
    def forward(cls, steps, curr_direction, curr_coordinates):
        if Direction.is_valid_direction(curr_direction):
            if curr_direction == "NORTH":
                x, y = curr_coordinates
                return x, y + steps
            elif curr_direction == "SOUTH":
                x, y = curr_coordinates
                return x, y - steps
            elif curr_direction == "EAST":
                x, y = curr_coordinates
                return x + steps, y
            elif curr_direction == "WEST":
                x, y = curr_coordinates
                return x - steps, y

        # if we cannot find any valid scenario
        # then just return existing coordinates
        return curr_coordinates


class Robot:
    """
    Create a moveable game object

    Note that collision detection is performed in Simulator class,
    not Robot class
    """

    def __init__(self):
        self.x, self.y = None, None
        self.direction = None
        self.is_initialized = False

    def get_location(self):
        return self.x, self.y

    def place(self, x, y, direction):
        self.is_initialized = True
        self.x, self.y = int(x), int(y)
        self.direction = direction
        return True

    def get_next_move(self):
        if self.is_initialized:
            next_x, next_y = Movement.forward(1, self.direction,
                                              self.get_location())
            return next_x, next_y
        return None, None

    def move(self):
        if self.is_initialized:
            self.x, self.y = self.get_next_move()
            return True
        return False

    def left(self):
        if self.is_initialized:
            self.direction = Direction.rotate_left(self.direction)
            return True
        return False

    def right(self):
        if self.is_initialized:
            self.direction = Direction.rotate_right(self.direction)
            return True
        return False

    def __repr__(self):
        if self.is_initialized:
            return "{},{},{}".format(self.x, self.y, self.direction)
        return ""


class Simulator:
    def __init__(self):
        self.table = Table()
        self.robot = Robot()
        self.table.init_square_table(5)
        # self.table.init_rectangle_table(6, 5)

    def place(self, x, y, direction):
        """
        Tries to validate coordinates and direction before placing robot

        returns True if operation succeeds
        """
        if Direction.is_valid_direction(direction):
            if self.table.is_valid_coordinate(x, y):
                return self.robot.place(x, y, direction)

        return False

    def move(self):
        """
        Try to get robot's next move and decide if robot should move

        returns True if move operation succeeds
        """
        next_x, next_y = self.robot.get_next_move()
        if self.table.is_valid_coordinate(next_x, next_y):
            return self.robot.move()

        return False

    def left(self):
        """
        returns True if robot can successfully turn left
        """
        return self.robot.left()

    def right(self):
        """
        returns True if robot can successfully turn left
        """
        return self.robot.right()

    def report(self):
        """
        returns robot status
        """
        return str(self.robot)


def main():
    sim = Simulator()
    table = sim.table
    print(table.valid_coordinates)

    print(table.is_valid_coordinate(-1, -3))
    print(table.is_valid_coordinate(0, 0))
    print(table.is_valid_coordinate(4, 4))
    print(table.is_valid_coordinate(4, 5))


if __name__ == '__main__':
    main()
