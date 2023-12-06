# Screen class for Karelbug game

import pygame
from Maze import Maze
from Buttons import Button
from Movements import Move

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

        """Initialize the player position
            coord_x and coord_y: initial position of the player
            speed_x and move_x: updates the position of the player in x axis
            speed_y and move_y: updates the position of the player in y axis
        """

        self.cord_x = 625
        self.cord_y = 550

        self.speed_x = 0
        self.speed_y = 0
        self.move_x = 0
        self.move_y = 0

        """Check if the player can move and restart the movement
            move: checks if the player can move
            pressed: check if the player use the play button
            can_restart: check if can restart the game
        """

        self.move = 0
        self.pressed = False
        self.can_restart = False

        """Initialize the movelist of the player
            movimientos: add and remove the movement list of the player
            all_movimientos: add and print the movement list of the player
        """

        self.movimientos = []
        self.all_movimientos = []

        """Initialize the actual limit colision of the player
        limit_x_min and limit_x_max: set the actual limit of x axis
        limit_y_min and limit_y_max: set the actual limit of y axis
        actual_limit: set the actual limit of the player
        """

        self.limit_x_min = 0
        self.limit_x_max = 1
        self.limit_y_min = 10
        self.limit_y_max = 11
        self.actual_limit = ((self.limit_x_min,self.limit_y_min),(self.limit_x_max,self.limit_y_min))

        #stop the player movement 
        self.stop = 0

        """
            direction: set the directions in cardinal flower
            direction2: set the direction in x and y axis
        """
        self.direction = ['E','S','W','N']
        self.direction2 = ['X','Y','-X','-Y']

        """Initialize the player view
            dview: get the actual view direction
            bug_view: get the player view direction
            last_view: check if the player view direction match the actual view direction
        """

        self.dview = self.direction[3]
        self.bug_view = self.direction[3]
        self.last_view = self.direction[3]

        """
            bugV: control the view direction of the player
            bugV: control the view direction of the player in order of the movement list
        """
        self.bugV = 3
        self.bugV2 = 3

        #Initialize the colition of elements
        self.walls_colition = []

        # pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

        """
            Initialize the spirtes and buttons of the game
        """
        self.up_img = pygame.image.load('Sprites\Arriba_btn.png').convert_alpha()

        self.turn_right_img = pygame.image.load('Sprites\Turn_Right_btn.png').convert_alpha()
        self.turn_left_img = pygame.image.load('Sprites\Turn_Left_btn.png').convert_alpha()

        self.up_mini_img = pygame.image.load('Sprites\Arriba_mini_btn.png').convert_alpha()

        self.turn_right_mini_img = pygame.image.load('Sprites\Turn_Right_mini_btn.png').convert_alpha()
        self.turn_left_mini_img = pygame.image.load('Sprites\Turn_Left_mini_btn.png').convert_alpha()

        self.play_img = pygame.image.load('Sprites\Play_btn.png').convert_alpha()

        self.reestart_img = pygame.image.load('Sprites\Reestart_btn.png').convert_alpha()

        self.bug_img = pygame.image.load('Sprites\Bug.png').convert_alpha()

        self.move_up_btn = Button(250,100,self.up_img,self.screen)

        self.turn_right_btn = Button(360,100,self.turn_right_img,self.screen)
        self.turn_left_btn = Button(140,100,self.turn_left_img,self.screen)

        self.play_btn = Button(250,220,self.play_img,self.screen)
        self.reestart_btn = Button(250,220,self.reestart_img,self.screen)

        # pygame setup
        self.clock = pygame.time.Clock()
        self.running = True
        self.maze = Maze()


    def run(self):
        """Run the game loop"""
        
        while self.running:
            self.update_maze()
            self.update_movements()

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("black")

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
                                    cosa = wall[0]
                                    cosa2 = wall[1]
                                    #remove the wall colition
                                    self.walls_colition.remove(((cosa[0],cosa[1]),(cosa2[0],cosa2[1])))
                            else:
                                #print("Not drawn yet")
                                self.maze.get_wall(wall).is_drawn = True
                                cosa = wall[0]
                                cosa2 = wall[1]
                                #add the wall colition
                                self.walls_colition.append(((cosa[0],cosa[1]),(cosa2[0],cosa2[1])))
                        
                        #print(self.maze.is_on_wall(pos[0], pos[1])) #UNCOMMENT THIS LINE TO SEE THE COORDINATES OF THE WALLS

            # Draw a white vertical line in the middle of the screen
            pygame.draw.line(self.screen, "white", (self.width / 2, 0), (self.width / 2, self.height))

            # Draw the player
            self.img_rect = self.bug_img.get_rect()
            self.img_rect.center = (self.cord_x+25, self.cord_y+25)
            self.screen.blit(self.bug_img, self.img_rect)

            # Draw and configure the buton turn left
            if self.turn_left_btn.draw():
                self.bugV -= 1
                if self.bugV < 0:
                    self.bugV = 3
                self.last_view = self.direction[self.bugV]
                self.movimientos.append(self.direction[self.bugV])
                self.all_movimientos.append('L')

            # Draw and configure the buton turn right
            if self.turn_right_btn.draw():
                self.bugV += 1
                if self.bugV > 3:
                    self.bugV = 0
                self.last_view = self.direction[self.bugV]
                self.movimientos.append(self.direction[self.bugV])
                self.all_movimientos.append('R')

            # Draw and configure the move button
            if self.move_up_btn.draw():
                if self.last_view == self.direction[0]:
                    self.movimientos.append('X')
                    self.all_movimientos.append('X')
                elif self.last_view == self.direction[1]:
                    self.movimientos.append('-Y')
                    self.all_movimientos.append('-Y')
                elif self.last_view == self.direction[2]:
                    self.movimientos.append('-X')
                    self.all_movimientos.append('-X')
                else:
                    self.movimientos.append('Y')
                    self.all_movimientos.append('Y')

            # check if can restart the game
            if self.can_restart == False:
                if self.play_btn.draw():
                    self.move = 1
                    self.pressed = True
                    self.can_restart = True
            else:
                # Draw and configure the restart button
                if self.reestart_btn.draw():
                    self.cord_x = 625
                    self.cord_y = 550
                    self.dview = self.direction[3]
                    while self.bug_view != self.dview:
                        self.bugV -= 1
                        if self.bugV < 0:
                            self.bugV = 3
                        self.bug_view = self.direction[self.bugV]
                        self.bug_img = pygame.transform.rotate(self.bug_img,90)
                    self.last_view = self.direction[3]
                    self.all_movimientos = []
                    self.movimientos = []
                    self.move = 0
                    self.bugV = 3
                    self.bugV2 = 3
                    self.limit_x_min = 0
                    self.limit_x_max = 1
                    self.limit_y_min = 10
                    self.limit_y_max = 11
                    self.is_blocked()
                    self.can_restart = False


            num = 0

            # Check if has wall colitions
            if self.walls_colition:
                while num < len(self.walls_colition):
                    # Stop the game if the actual limit is in wall colitions
                    if self.actual_limit == self.walls_colition[num]:
                        self.speed_y = 0
                        self.speed_x = 0
                        self.move_x = 0
                        self.move_y = 0
                        self.pressed = False
                        self.move = 0
                    else:
                        self.stop = 1
                    num += 1
                num = 0

            # Check if can move
            if self.move_x == 0 and self.move_y == 0 and self.move == 1: 
                # Check if the player has movements
                if self.movimientos:
                    # Check if the player moves to right
                    if self.move == 1 and self.movimientos[0] == 'X':
                        self.move_x = 50
                        self.speed_x = 5
                        self.move = 0
                        self.limit_x_min += 1
                        self.limit_x_max += 1
                        self.is_blocked()

                    # Check if the player moves to left
                    elif self.move == 1 and self.movimientos[0]  == '-X':
                        self.move_x = 50
                        self.speed_x = -5
                        self.move = 0
                        self.limit_x_min += 1
                        self.limit_x_max += 1
                        self.is_blocked()
                        
                    # Check if the player moves to the bottom
                    elif self.move == 1 and self.movimientos[0]  == 'Y':
                        self.move_y = 50
                        self.speed_y = -5
                        self.move = 0
                        self.limit_y_min -= 1
                        self.limit_y_max -= 1
                        self.is_blocked()
                        
                    # Check if the player moves up
                    elif self.move == 1 and self.movimientos[0] == '-Y':
                        self.move_y = 50
                        self.speed_y = 5
                        self.move = 0
                        self.limit_y_min += 1
                        self.limit_y_max += 1
                        self.is_blocked()
                        
                    # Check if the player rotates or remove the previus move from the move list
                    if self.movimientos[0] not in self.direction:
                        self.movimientos.remove(self.movimientos[0])
                    else:
                        # Check if the player needs to rotate
                        if self.bug_view != self.movimientos[0]:
                            self.bugV2 -= 1
                            if self.bugV2 < 0:
                                self.bugV2 = 3
                            self.bug_view =  self.direction[self.bugV2]
                            self.bug_img = pygame.transform.rotate(self.bug_img,90)
                        else:
                            self.is_blocked()
                            self.movimientos.remove(self.movimientos[0])

                    # Check if the player can move
                    if len(self.movimientos) > 1:
                        if self.stop == 1 and self.movimientos[1] in self.direction2:
                            if self.actual_limit in self.walls_colition:
                                self.speed_y = 0
                                self.speed_x = 0
                                self.move_x = 0
                                self.move_y = 0
                                self.pressed = False
                                self.move = 0
                                self.stop = 0
                                
            # Update the player position
            else:
                #check if the next player move is in the limits of the maze
                if self.move_x > 0 and self.cord_x >= 625 and self.cord_x <= 1125:
                    self.move_x -= 5
                    self.cord_x += self.speed_x
                else:
                    self.move_x = 0
                    self.speed_x = 0

                if self.move_x == 0:
                    self.speed_x = 0

                #check if the next player move is in the limits of the maze
                if self.move_y > 0 and self.cord_y >= 50 and self.cord_y <= 550:
                    self.move_y -= 5
                    self.cord_y += self.speed_y 
                else:
                    self.move_y = 0
                    self.speed_y = 0

                if self.move_y == 0:
                    self.speed_y = 0
                
                if self.movimientos and self.pressed:
                    self.move = 1 
                else:
                    if self.move_x == 0 and self.move_y == 0:
                        self.move = 0
                        self.pressed = False

            # Draw the corners of the maze on the right side of the screen
            self.update_movements()
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

    #update and show the move list
    def update_movements(self):

        move_cord_x = 100
        move_cord_y = 400

        for move in range(len(self.all_movimientos)):
            if self.all_movimientos[move] in self.direction2:
                Move(move_cord_x,move_cord_y,self.up_mini_img,self.screen).draw()
            elif self.all_movimientos[move] == 'L':
                Move(move_cord_x,move_cord_y,self.turn_left_mini_img,self.screen).draw()
            elif self.all_movimientos[move] == 'R':
                Move(move_cord_x,move_cord_y,self.turn_right_mini_img,self.screen).draw()

            move_cord_x += 30
            if move_cord_x > 500:
                move_cord_y += 30
                move_cord_x = 100

    #check if the player is in front of a colition
    def is_blocked(self):
        if self.bug_view == 'E':
            self.actual_limit = ((self.limit_x_min,self.limit_y_min),(self.limit_x_min,self.limit_y_max))
        if self.bug_view == 'S':
            self.actual_limit = ((self.limit_x_min,self.limit_y_max),(self.limit_x_max,self.limit_y_max))
        if self.bug_view == 'W':
            self.actual_limit = ((self.limit_x_min,self.limit_y_min),(self.limit_x_min,self.limit_y_max))
        if self.bug_view == 'N':
            self.actual_limit = ((self.limit_x_min,self.limit_y_max),(self.limit_x_max,self.limit_y_max))