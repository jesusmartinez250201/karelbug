class Buzzer:
    """
    A Buzzer object represents a buzzer in the Karel maze.
    """
    def __init__(self, coord_x, coord_y, is_drawn=False):
        """
        Initialize a buzzer.
        params:
            coord_x: x coordinate of the buzzer
            coord_y: y coordinate of the buzzer
            is_drawn: whether the buzzer is drawn or not
        """
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.is_drawn = is_drawn
    
    def get_coordinates(self):
        """
        Get the coordinates of the buzzer.
        returns:
            Tuple with the coordinates of the buzzer (coord_x, coord_y)
        """
        return (self.coord_x, self.coord_y)
        