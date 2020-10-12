class Table:
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
        if (x, y) in self.valid_coordinates:
            return True
        return False


class Robot:
    def __init__(self):
        self.x = None
        self.y = None
        self.direction = None
        self.is_initialized = None

    def place(self, x, y, direction):
        self.is_initialized = True
        self.x = x
        self.y = y
        self.direction = direction
        return True

    def move(self):
        if self.is_initialized:
            pass

        return True

    def left(self):
        pass

    def right(self):
        pass

    def __str__(self):
        if self.is_initialized:
            return "{} {} {}".format(self.x, self.y, self.direction)

        return ""


class Simulator:
    def __init__(self):
        self.table = Table()
        # self.table.init_square_table(5)
        self.table.init_rectangle_table(6, 5)

        self.robot = Robot()


def main():
    sim = Simulator()
    table = sim.table
    print(table.valid_coordinates)

    print(table.is_valid_coordinate(-1, -3))
    print(table.is_valid_coordinate(0, 0))
    print(table.is_valid_coordinate(4, 4))
    print(table.is_valid_coordinate(4, 5))
    # import pdb
    # pdb.set_trace()


if __name__ == '__main__':
    main()
