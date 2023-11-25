class Wall:
    """
    A Wall object represents a wall in the Karel maze.
    """
    def __init__(self, x_start, y_start, x_end, y_end, is_drawn=False, is_edge=False):
        """
        Initialize a wall.
        params:
            x_start: x coordinate of the start of the wall
            y_start: y coordinate of the start of the wall
            x_end: x coordinate of the end of the wall
            y_end: y coordinate of the end of the wall
            is_drawn: whether the wall is drawn or not
            is_edge: whether the wall is an edge wall or not
        """
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.is_drawn = is_drawn
        self.is_edge = is_edge
    
    def get_coordinates(self):
        """
        Get the coordinates of the wall.
        returns:
            Tuple with the coordinates of the wall (x_start, y_start, x_end, y_end)
        """
        return ((self.x_start, self.y_start), (self.x_end, self.y_end))
        