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

        self.cord_x = 625
        self.cord_y = 550

        self.speed_x = 0
        self.speed_y = 0
        self.move_x = 0
        self.move_y = 0

        self.move = 0
        self.pressed = False
        self.can_restart = False

        self.movimientos = []
        self.all_movimientos = []

        self.direction = ['E','S','W','N']
        self.direction2 = ['X','Y','-X','-Y']

        self.dview = self.direction[3]
        self.bug_view = self.direction[3]
        self.last_view = self.direction[3]

        self.bugV = 3
        self.bugV2 = 3

        # pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

        #self.right_img = pygame.image.load('Sprites\Right_btn.png').convert_alpha()
        #self.left_img = pygame.image.load('Sprites\Left_btn.png').convert_alpha()
        self.up_img = pygame.image.load('Sprites\Arriba_btn.png').convert_alpha()
        #self.down_img = pygame.image.load('Sprites\Down_btn.png').convert_alpha()

        self.turn_right_img = pygame.image.load('Sprites\Turn_Right_btn.png').convert_alpha()
        self.turn_left_img = pygame.image.load('Sprites\Turn_Left_btn.png').convert_alpha()

        self.up_mini_img = pygame.image.load('Sprites\Arriba_mini_btn.png').convert_alpha()

        self.turn_right_mini_img = pygame.image.load('Sprites\Turn_Right_mini_btn.png').convert_alpha()
        self.turn_left_mini_img = pygame.image.load('Sprites\Turn_Left_mini_btn.png').convert_alpha()

        self.play_img = pygame.image.load('Sprites\Play_btn.png').convert_alpha()

        self.reestart_img = pygame.image.load('Sprites\Reestart_btn.png').convert_alpha()

        self.bug_img = pygame.image.load('Sprites\Bug.png').convert_alpha()

        self.move_up_btn = Button(250,100,self.up_img,self.screen)
        #self.move_left_btn = Button(140,160,self.left_img,self.screen)
        #self.move_down_btn = Button(250,160,self.down_img,self.screen)
        #self.move_right_btn = Button(360,160,self.right_img,self.screen)

        self.turn_right_btn = Button(360,100,self.turn_right_img,self.screen)
        self.turn_left_btn = Button(140,100,self.turn_left_img,self.screen)

        self.play_btn = Button(250,220,self.play_img,self.screen)
        self.reestart_btn = Button(250,220,self.reestart_img,self.screen)

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
                            else:
                                #print("Not drawn yet")
                                self.maze.get_wall(wall).is_drawn = True
                                #self.update_maze()

                        #print(self.maze.is_on_wall(pos[0], pos[1])) #UNCOMMENT THIS LINE TO SEE THE COORDINATES OF THE WALLS

            # Draw a white vertical line in the middle of the screen
            pygame.draw.line(self.screen, "white", (self.width / 2, 0), (self.width / 2, self.height))

            img_rect = self.bug_img.get_rect()
            img_rect.center = (self.cord_x+25, self.cord_y+25)
            self.screen.blit(self.bug_img, img_rect)
            #pygame.draw.rect(self.screen, "red", (self.cord_x+5, self.cord_y+5, 40, 40))

            if self.turn_left_btn.draw():
                self.bugV -= 1
                if self.bugV < 0:
                    self.bugV = 3
                self.last_view = self.direction[self.bugV]
                self.movimientos.append(self.direction[self.bugV])
                self.all_movimientos.append('L')

            if self.turn_right_btn.draw():
                self.bugV += 1
                if self.bugV > 3:
                    self.bugV = 0
                self.last_view = self.direction[self.bugV]
                self.movimientos.append(self.direction[self.bugV])
                self.all_movimientos.append('R')

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

            if self.can_restart == False:
                if self.play_btn.draw():
                    self.move = 1
                    self.pressed = True
                    self.can_restart = True
            else:
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
                    self.can_restart = False

            if self.move_x == 0 and self.move_y == 0 and self.move == 1: 
                if self.movimientos:
                    if self.move == 1 and self.movimientos[0] == 'X':
                        self.move_x = 50
                        self.speed_x = 5
                        self.move = 0

                    elif self.move == 1 and self.movimientos[0]  == '-X':
                        self.move_x = 50
                        self.speed_x = -5
                        self.move = 0
                        
                    elif self.move == 1 and self.movimientos[0]  == 'Y':
                        self.move_y = 50
                        self.speed_y = -5
                        self.move = 0
                        
                    elif self.move == 1 and self.movimientos[0] == '-Y':
                        self.move_y = 50
                        self.speed_y = 5
                        self.move = 0
                        
                    if self.movimientos[0] not in self.direction:
                        self.movimientos.remove(self.movimientos[0])
                    else:
                        if self.bug_view != self.movimientos[0]:
                            self.bugV2 -= 1
                            if self.bugV2 < 0:
                                self.bugV2 = 3
                            self.bug_view =  self.direction[self.bugV2]
                            self.bug_img = pygame.transform.rotate(self.bug_img,90)
                        else:
                            self.movimientos.remove(self.movimientos[0])
            else:
                if self.move_x > 0 and self.cord_x >= 625 and self.cord_x <= 1100:
                    self.move_x -= 5
                    self.cord_x += self.speed_x
                else:
                    self.move_x = 0
                    self.speed_x = 0

                if self.move_x == 0:
                    self.speed_x = 0
                
                if self.move_y > 0 and self.cord_y >= 75 and self.cord_y <= 550:
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

