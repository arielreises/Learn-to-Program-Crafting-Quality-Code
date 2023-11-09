# UofT - University of Toronto
# Course - Learn to Program: Crafting Quality Code
# Student: Ariel Ladislau Reises
# Github: github.com/arielreises

# Constants for the contents of the maze.
WALL = '#'
HALL = '.'
SPROUT = '@'
LEFT = -1
RIGHT = 1
NO_CHANGE = 0
UP = -1
DOWN = 1
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'

class Rat:
    """ A rat caught in a maze. """

    def __init__(self, symbol, row, col):
        """ Initialize the rat's instance variables. """
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        """ Set the rat's location. """
        self.row = row
        self.col = col

    def eat_sprout(self):
        """ Increase the number of sprouts eaten by the rat. """
        self.num_sprouts_eaten += 1

    def __str__(self):
        """ Return a string representation of the rat. """
        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(
            self.symbol, self.row, self.col, self.num_sprouts_eaten)

class Maze:
    """ A 2D maze. """

    def __init__(self, maze, rat_1, rat_2):
        """ Initialize the maze's instance variables. """
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = sum(row.count(SPROUT) for row in maze)

    def is_wall(self, row, col):
        """ Return True if there is a wall at the given row and column. """
        return self.maze[row][col] == WALL

    def get_character(self, row, col):
        """ Return the character in the maze at the given row and column. """
        return self.maze[row][col]

    def move(self, rat, vertical, horizontal):
        """ Move the rat in the given direction, unless there is a wall. """
        new_row = rat.row + vertical
        new_col = rat.col + horizontal

        if not self.is_wall(new_row, new_col):
            if self.maze[new_row][new_col] == SPROUT:
                rat.eat_sprout()
                self.num_sprouts_left -= 1

            rat.set_location(new_row, new_col)
            return True

        return False

    def __str__(self):
        """ Return a string representation of the maze. """
        result = ''
        for row in self.maze:
            result += ''.join(row) + '\n'
        result += str(self.rat_1) + '\n' + str(self.rat_2)
        return result
