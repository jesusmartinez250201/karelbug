from Corner import Corner
from Wall import Wall

class Maze:
    """Class that represents the maze in the Karel game"""
    def __init__(self):
        """Initialize the maze
        attributes:
            maze: matrix that represents the maze
            """
        self.corners = []
        self.walls = []
        self.generate_corners()
        self.generate_walls()

    def generate_corners(self):
        """Generate the corners of the maze"""
        for x in range(12):
            self.corners.append([])
            for y in range(12):
                self.corners[x].append(Corner(x, y))

    def generate_walls(self):
        """Generate the walls of the maze"""
        for corner_row in self.corners:
            for corner in corner_row:
                # Draw horizontal walls
                if corner.x < 11 and corner.y == 0:
                    self.walls.append(Wall(corner.x, corner.y, corner.x + 1, corner.y, False, True))
                elif corner.x < 11 and corner.y == 11:
                    self.walls.append(Wall(corner.x, corner.y, corner.x + 1, corner.y, False, True))
                else:
                    self.walls.append(Wall(corner.x, corner.y, corner.x + 1, corner.y))
                # Draw vertical walls
                if corner.x == 11 and corner.y < 11:
                    self.walls.append(Wall(corner.x, corner.y, corner.x, corner.y + 1, False, True))
                elif corner.x == 0 and corner.y < 11:
                    self.walls.append(Wall(corner.x, corner.y, corner.x, corner.y + 1, False, True))
                else:
                    self.walls.append(Wall(corner.x, corner.y, corner.x, corner.y + 1))
        


    def is_on_wall(self, x, y, tolerance=10):
        """Check if the given coordinates are on a wall
        params:
            x: x coordinate
            y: y coordinate
        returns:
            Tuple with the corners of the wall if the coordinates are on a wall, False otherwise"""
        for wall in self.walls:
            if wall.is_edge:
                if wall.x_start == wall.x_end:
                    min_x = wall.x_start * 50 + 625 - tolerance
                    max_x = wall.x_start * 50 + 625 + tolerance
                    min_y = min(wall.y_start, wall.y_end) * 50 + 50
                    max_y = max(wall.y_start, wall.y_end) * 50 + 50
                    if min_x <= x <= max_x and min_y <= y <= max_y:
                        return ((wall.x_start, wall.y_start), (wall.x_end, wall.y_end))
                else:
                    min_x = min(wall.x_start, wall.x_end) * 50 + 625
                    max_x = max(wall.x_start, wall.x_end) * 50 + 625
                    min_y = wall.y_start * 50 + 50 - tolerance
                    max_y = wall.y_start * 50 + 50 + tolerance
                    if min_x <= x <= max_x and min_y <= y <= max_y:
                        return ((wall.x_start, wall.y_start), (wall.x_end, wall.y_end))
            else:
                if wall.x_start == wall.x_end:
                    min_x = wall.x_start * 50 + 625 - tolerance
                    max_x = wall.x_start * 50 + 625 + tolerance
                    min_y = min(wall.y_start, wall.y_end) * 50 + 50
                    max_y = max(wall.y_start, wall.y_end) * 50 + 50
                    if min_x <= x <= max_x and min_y <= y <= max_y:
                        return ((wall.x_start, wall.y_start), (wall.x_end, wall.y_end))
                else:
                    min_x = min(wall.x_start, wall.x_end) * 50 + 625
                    max_x = max(wall.x_start, wall.x_end) * 50 + 625
                    min_y = wall.y_start * 50 + 50 - tolerance
                    max_y = wall.y_start * 50 + 50 + tolerance
                    if min_x <= x <= max_x and min_y <= y <= max_y:
                        return ((wall.x_start, wall.y_start), (wall.x_end, wall.y_end))
        return False
    
    def get_corner(self, x, y):
        """Get the corner at the given coordinates
        params:
            x: x coordinate
            y: y coordinate
        returns:
            Corner at the given coordinates"""
        return self.corners[x][y]
    
    def get_wall(self, position):
        """Get the wall at the given position
        params:
            position: tuple with the coordinates of the wall (x_start, y_start, x_end, y_end)
        returns:
            Wall object at the given position"""
        for wall in self.walls:
            if wall.get_coordinates() == position:
                return wall
        return False
            



