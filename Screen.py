# Screen class for Karelbug game

import pygame
from Maze import Maze

class Screen:
    """Screen class for Karelbug game"""
    def __init__(self, width, height, title):
        """Initialize the game screen
        params:
            width: width of the screen in pixels
            height: height of the screen in pixels
            title: title of the window"""
        self.width = width
        self.height = height
        self.title = title

        # pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        self.running = True
        self.maze = Maze()

    

    def run(self):
        """Run the game loop"""
        while self.running:
            self.update_maze()
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                # Get the clicked event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the position of the mouse
                    pos = pygame.mouse.get_pos()
                    # Check if the mouse is on the right side of the screen
                    if pos[0] > self.width / 2:
                        # Check if the mouse is between two corners
                        wall = self.maze.is_on_wall(pos[0], pos[1])
                        if wall:
                            if self.maze.get_wall(wall).is_drawn:
                                #print("Wall already drawn")
                                if not self.maze.get_wall(wall).is_edge:
                                    self.maze.get_wall(wall).is_drawn = False
                            else:
                                #print("Not drawn yet")
                                self.maze.get_wall(wall).is_drawn = True
                                #self.update_maze()
                        #print(self.maze.is_on_wall(pos[0], pos[1])) UNCOMMENT THIS LINE TO SEE THE COORDINATES OF THE WALLS
                        
            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("black")

            # Draw a white vertical line in the middle of the screen
            pygame.draw.line(self.screen, "white", (self.width / 2, 0), (self.width / 2, self.height))

            # Draw the corners of the maze on the right side of the screen
            self.update_maze()
            
            # flip() the display to put your work on screen
            pygame.display.flip()

            self.clock.tick(60)  # limits FPS to 60

        pygame.quit()

    def update_maze(self):
        """Redraw the maze"""
        for row in self.maze.corners:
                for corner in row:
                    pygame.draw.circle(self.screen, "white", (corner.x * 50 + 625, corner.y * 50 + 50), 5)
            # Draw the walls of the maze on the right side of the screen
        for wall in self.maze.walls:
            # Draw only the walls that are edge walls
            if wall.is_edge or wall.is_drawn:
                pygame.draw.line(self.screen, "white", (wall.x_start * 50 + 625, wall.y_start * 50 + 50), (wall.x_end * 50 + 625, wall.y_end * 50 + 50))
                #wall.is_drawn = True