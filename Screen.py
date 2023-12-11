

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
            count_while: check the how many cicles the player has
        """

        self.move = 0
        self.pressed = False
        self.can_restart = False
        self.count_while = 0
        self.count_while2 = 0

        """Initialize the movelist of the player
            movimientos: add and remove the movement list of the player
            all_movimientos: add and print the movement list of the player
            while: actions: add the movements of the cicle list
        """

        self.movimientos = []
        self.all_movimientos = []
        self.while_actions = []
        self.while_condition = []

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
        self.left_limit = ((self.limit_x_min,self.limit_y_min),(self.limit_x_min,self.limit_y_max))
        self.right_limit = ((self.limit_x_max,self.limit_y_min),(self.limit_x_max,self.limit_y_max))

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
        self.prev_view = self.last_view

        """
            bugV: control the view direction of the player
            bugV: control the view direction of the player in order of the movement list
        """
        self.bugV = 3
        self.bugV2 = 3

        #Initialize the colition of elements
        self.walls_colition = []
        self.limits_colition = [((0, 10), (0, 11)), ((0, 9), (0, 10)), ((0, 8), (0, 9)), 
        ((0, 7), (0, 8)), ((0, 6), (0, 7)), ((0, 5), (0, 6)), ((0, 4), (0, 5)), ((0, 3), (0, 4)), 
        ((0, 2), (0, 3)), ((0, 1), (0, 2)), ((0, 0), (0, 1)), ((0, 0), (1, 0)), ((1, 0), (2, 0)), 
        ((2, 0), (3, 0)), ((3, 0), (4, 0)), ((4, 0), (5, 0)), ((5, 0), (6, 0)), ((6, 0), (7, 0)), 
        ((7, 0), (8, 0)), ((8, 0), (9, 0)), ((9, 0), (10, 0)), ((10, 0), (11, 0)), ((11, 0), (11, 1)), 
        ((11, 1), (11, 2)), ((11, 2), (11, 3)), ((11, 3), (11, 4)), ((11, 4), (11, 5)), ((11, 5), (11, 6)), 
        ((11, 6), (11, 7)), ((11, 7), (11, 8)), ((11, 8), (11, 9)), ((11, 9), (11, 10)), ((11, 10), (11, 11)), 
        ((10, 11), (11, 11)), ((9, 11), (10, 11)), ((8, 11), (9, 11)), ((7, 11), (8, 11)), ((6, 11), (7, 11)), 
        ((5, 11), (6, 11)), ((4, 11), (5, 11)), ((3, 11), (4, 11)), ((2, 11), (3, 11)), ((1, 11), (2, 11))]

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

        self.up_w_img = pygame.image.load('Sprites\Arriba_w_btn.png').convert_alpha()
        self.turn_right_w_img = pygame.image.load('Sprites\Turn_Right_w_btn.png').convert_alpha()
        self.turn_left_w_img = pygame.image.load('Sprites\Turn_Left_w_btn.png').convert_alpha()

        self.wall_on_right_img = pygame.image.load('Sprites\Wall_on_right_btn.png').convert_alpha()
        self.wall_on_left_img = pygame.image.load('Sprites\Wall_on_left_btn.png').convert_alpha()
        self.wall_in_front_img = pygame.image.load('Sprites\Wall_btn.png').convert_alpha()

        self.wall_on_right_mini_img = pygame.image.load('Sprites\Wall_on_right_mini_btn.png').convert_alpha()
        self.wall_on_left_mini_img = pygame.image.load('Sprites\Wall_on_left_mini_btn.png').convert_alpha()     
        self.wall_in_front_mini_img = pygame.image.load('Sprites\Wall_mini_btn.png').convert_alpha()   

        self.up_mini_img = pygame.image.load('Sprites\Arriba_mini_btn.png').convert_alpha()
        self.turn_right_mini_img = pygame.image.load('Sprites\Turn_Right_mini_btn.png').convert_alpha()
        self.turn_left_mini_img = pygame.image.load('Sprites\Turn_Left_mini_btn.png').convert_alpha()

        self.up_mini_w_img = pygame.image.load('Sprites\Arriba_w_mini_btn.png').convert_alpha()
        self.turn_right_w_mini_img = pygame.image.load('Sprites\Turn_Right_w_mini_btn.png').convert_alpha()
        self.turn_left_w_mini_img = pygame.image.load('Sprites\Turn_Left_w_mini_btn.png').convert_alpha()

        self.play_img = pygame.image.load('Sprites\Play_btn.png').convert_alpha()
        self.reestart_img = pygame.image.load('Sprites\Reestart_btn.png').convert_alpha()

        self.while_img = pygame.image.load('Sprites\While_btn.png').convert_alpha()
        self.while_mini_img = pygame.image.load('Sprites\While_mini_btn.png').convert_alpha()

        self.bug_img = pygame.image.load('Sprites\Bug.png').convert_alpha()


        self.move_up_btn = Button(250,100,self.up_img,self.screen)
        self.turn_right_btn = Button(360,100,self.turn_right_img,self.screen)
        self.turn_left_btn = Button(140,100,self.turn_left_img,self.screen)

        self.play_btn = Button(250,220,self.play_img,self.screen)
        self.reestart_btn = Button(360,220,self.reestart_img,self.screen)

        self.while_btn = Button(30, 100, self.while_img, self.screen)

        self.end_while_btn = Button(30, 100, self.while_img, self.screen)
        self.wall_on_left_btn = Button(140, 50, self.wall_on_left_img, self.screen)
        self.wall_on_right_btn = Button(360, 50, self.wall_on_right_img, self.screen)
        self.wall_in_front_btn = Button(250, 50, self.wall_in_front_img, self.screen)

        # pygame setup
        self.clock = pygame.time.Clock()
        self.running = True
        self.maze = Maze()


    def run(self):

        self.while_btn_enabled = True
        self.end_while_btn_enabled = False
        self.wall_on_left_btn_enabled = False
        self.wall_on_right_btn_enabled = False
        self.wall_in_front_btn_enabled = False
        self.wall_con = True

        while self.running:
            self.update_maze()
            self.update_movements()

            self.screen.fill("black")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pos[0] > self.width / 2:
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
                        
            pygame.draw.line(self.screen, "white", (self.width / 2, 0), (self.width / 2, self.height))

            self.img_rect = self.bug_img.get_rect()
            self.img_rect.center = (self.cord_x + 25, self.cord_y + 25)
            self.screen.blit(self.bug_img, self.img_rect)

            if self.end_while_btn_enabled:
                self.move_up_btn.update_image(self.up_w_img)
                self.turn_right_btn.update_image(self.turn_right_w_img)
                self.turn_left_btn.update_image(self.turn_left_w_img)
            else:
                self.move_up_btn.update_image(self.up_img)
                self.turn_right_btn.update_image(self.turn_right_img)
                self.turn_left_btn.update_image(self.turn_left_img)

            if self.wall_con and self.turn_left_btn.draw():
                if self.end_while_btn_enabled:
                    if len(self.while_actions) <= self.count_while:
                        self.while_actions.append([])
                    self.handle_while_button_click("Turn Left")
                else:
                    self.handle_button_click("turn_left")

            if self.wall_con and self.turn_right_btn.draw():
                if self.end_while_btn_enabled:
                    if len(self.while_actions) <= self.count_while:
                        self.while_actions.append([])
                    self.handle_while_button_click("Turn Right")
                else:
                    self.handle_button_click("turn_right")

            """if self.wall_con and self.if_btn.draw():
                self.movimientos.append('I')
                self.all_movimientos.append('I')"""

            if self.wall_con and self.move_up_btn.draw():
                if self.end_while_btn_enabled:
                    if len(self.while_actions) <= self.count_while:
                        self.while_actions.append([])
                    self.handle_while_button_click("Move Up")
                else:
                    self.handle_button_click("move_up")

            if self.can_restart == False and self.while_btn_enabled and self.play_btn.draw():
                    self.handle_button_click("play")
            
            if self.can_restart == True and self.while_btn_enabled and self.reestart_btn.draw():
                    self.handle_button_click("restart")

            if self.while_btn_enabled and self.while_btn.draw():
                self.while_btn_enabled = False
                self.end_while_btn_enabled = True
                self.wall_on_left_btn_enabled = True
                self.wall_on_right_btn_enabled = True
                self.wall_in_front_btn_enabled = True
                self.wall_con = False
                self.movimientos.append('Wh')
                self.all_movimientos.append('Wh')

            # Draw and configure the end_while button
            if self.end_while_btn_enabled and self.wall_con and self.end_while_btn.draw():
                self.handle_while_button_click("end_while")

            # Draw and configure the wall_on_left button
            if self.wall_on_left_btn_enabled and self.wall_con is False and self.wall_on_left_btn.draw():
                self.wall_con = True
                self.wall_on_left_btn_enabled = False
                self.wall_on_right_btn_enabled = False
                self.wall_in_front_btn_enabled = False
                self.handle_while_button_click("wall_on_left")

            # Draw and configure the wall_on_right button
            if self.wall_on_right_btn_enabled and self.wall_con is False and self.wall_on_right_btn.draw():
                self.wall_con = True
                self.wall_on_left_btn_enabled = False
                self.wall_on_right_btn_enabled = False
                self.wall_in_front_btn_enabled = False
                self.handle_while_button_click("wall_on_right")

            # Draw and configure the wall_in_front button
            if self.wall_in_front_btn_enabled and self.wall_con is False and self.wall_in_front_btn.draw():
                self.wall_con = True
                self.wall_on_left_btn_enabled = False
                self.wall_on_right_btn_enabled = False
                self.wall_in_front_btn_enabled = False
                self.handle_while_button_click("wall_in_front")

            num = 0

            if self.walls_colition:
                while num < len(self.walls_colition):
                    print(self.walls_colition, self.actual_limit)
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

            if self.move_x == 0 and self.move_y == 0 and self.move == 1:
                if self.movimientos:
                    #print(self.cord_x,self.cord_y)
                    #print(self.actual_limit,self.walls_colition)
                    if self.movimientos[0] == 'Wh':
                        #if self.left_limit in self.walls_colition or self.left_limit in self.limits_colition:
                        if self.count_while2 > len(self.while_actions[0])-1:
                            self.count_while2 = 0
                        if self.move == 1 and self.while_actions[0][self.count_while2] == "M":
                            if self.last_view == self.direction[0]:
                                self.handle_while_movement('X')
                                self.is_blocked()
                            elif self.last_view == self.direction[2]:
                                self.handle_while_movement('-X')
                                self.is_blocked()
                            elif self.last_view == self.direction[1]:
                                self.handle_while_movement('-Y')
                                self.is_blocked()
                            else:
                                self.handle_while_movement('Y')
                                self.is_blocked()
                        elif self.move == 1 and self.while_actions[0][self.count_while2] == "L":
                                self.handle_while_movement('L')
                        elif self.move == 1 and self.while_actions[0][self.count_while2] == "R":
                                self.handle_while_movement('R')                  

                        if self.stop == 1 and self.while_actions[0][self.count_while2] in self.direction2:
                            if self.actual_limit in self.walls_colition:
                                self.movimientos.remove((self.movimientos[0]))
                                

                        self.count_while2 += 1

                        if self.prev_view != self.last_view:
                            self.is_blocked()
                            print(self.actual_limit, (self.cord_x,self.cord_y))
                        
                        #print(self.cord_x, self.cord_y)
                        if self.cord_x in [620, 625] and self.last_view == "W" or self.cord_x in [1125, 1130] and self.last_view == "E":
                            self.movimientos.remove(self.movimientos[0])
                            print(self.movimientos)

                        print(self.last_view)
                        if self.cord_y in [45, 50] and self.last_view == "N" or self.cord_y in [550] and self.last_view == "S":
                            self.movimientos.remove(self.movimientos[0])
                            print(self.movimientos)

                    else:
                        if self.move == 1 and self.movimientos[0] == 'X':
                            self.move_x = 50
                            self.speed_x = 5
                            self.move = 0
                            self.limit_x_min += 1
                            self.limit_x_max += 1
                            self.is_blocked()

                        elif self.move == 1 and self.movimientos[0] == '-X':
                            self.move_x = 50
                            self.speed_x = -5
                            self.move = 0
                            self.limit_x_min += 1
                            self.limit_x_max += 1
                            self.is_blocked()

                        elif self.move == 1 and self.movimientos[0] == 'Y':
                            self.move_y = 50
                            self.speed_y = -5
                            self.move = 0
                            self.limit_y_min -= 1
                            self.limit_y_max -= 1
                            self.is_blocked()

                        elif self.move == 1 and self.movimientos[0] == '-Y':
                            self.move_y = 50
                            self.speed_y = 5
                            self.move = 0
                            self.limit_y_min += 1
                            self.limit_y_max += 1
                            self.is_blocked()

                        if self.movimientos[0] not in self.direction:
                            self.movimientos.remove(self.movimientos[0])
                        else:
                            if self.bug_view != self.movimientos[0]:
                                self.bugV2 -= 1
                                if self.bugV2 < 0:
                                    self.bugV2 = 3
                                self.bug_view = self.direction[self.bugV2]
                                self.bug_img = pygame.transform.rotate(self.bug_img, 90)
                            else:
                                self.is_blocked()
                                self.movimientos.remove(self.movimientos[0])

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

            else:
                if self.move_x > 0 and self.cord_x >= 625 and self.cord_x <= 1125:
                    self.move_x -= 5
                    self.cord_x += self.speed_x
                else:
                    self.move_x = 0
                    self.speed_x = 0                        

                if self.move_x == 0:
                    self.speed_x = 0

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

            self.update_maze()
            self.update_movements()

            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()


        pygame.quit()

    def handle_button_click(self, button):
        if button == "turn_left":
            self.turn_left()
        elif button == "turn_right":
            self.turn_right()
        elif button == "move_up":
            self.move_up()
        elif button == "play":
            self.play()
        elif button == "restart":
            self.restart()

    def handle_while_button_click(self, action):
        if action == "end_while":
            # Terminar el ciclo
            self.while_btn_enabled = True
            self.end_while_btn_enabled = False
            self.wall_on_left_btn_enabled = False
            self.wall_on_right_btn_enabled = False
            self.wall_in_front_btn_enabled = False
            # ... Agregar lógica para procesar las acciones del jugador durante el ciclo
            print("Actions during while loop:", self.while_actions)
            for wh in self.while_actions:
                if not wh:
                    self.count_while -= 1
                    self.movimientos.pop()
                    self.all_movimientos.pop()

            wh_t = [wh for wh in self.while_actions if wh]

            if not wh_t:
                if self.movimientos:
                    self.movimientos.pop()
                if self.all_movimientos:
                    self.all_movimientos.pop()

            self.while_actions = wh_t
            
            self.count_while += 1
            self.while_actions.append([])
        elif action in ["Turn Left", "Turn Right", "Move Up"]:
            if len(self.while_actions) <= self.count_while:
                self.while_actions.append([])
            if action in ["Turn Left", "Turn Right"]:
                if action == "Turn Left":
                    self.while_actions[self.count_while].append('L')
                else:
                    self.while_actions[self.count_while].append('R')
            else:
                self.while_actions[self.count_while].append('M')
            
        elif action in ["wall_on_left", "wall_on_right", "wall_in_front"]:
            if len(self.while_actions) <= self.count_while:
                self.while_actions.append([])
            self.while_actions[self.count_while].append(action)
            if len(self.while_condition) <= self.count_while:
                self.while_condition.append([])
            self.while_condition[self.count_while].append(action)

    def handle_while_movement(self, move):
        if move == "X":
            self.move_x = 50
            self.speed_x = 5
            self.move = 0
            self.limit_x_min += 1
            self.limit_x_max += 1
            
        elif move == '-X':
            self.move_x = 50
            self.speed_x = -5
            self.move = 0
            self.limit_x_min -= 1
            self.limit_x_max -= 1
            
        elif move == 'Y':
            self.move_y = 50
            self.speed_y = -5
            self.move = 0
            self.limit_y_min -= 1
            self.limit_y_max -= 1
            
        elif move == '-Y':
            self.move_y = 50
            self.speed_y = 5
            self.move = 0
            self.limit_y_min += 1
            self.limit_y_max += 1
            
        elif move == 'L':
            self.bugV -= 1
            if self.bugV < 0:
                self.bugV = 3
            self.prev_view = self.last_view
            self.last_view = self.direction[self.bugV]
            self.bug_img = pygame.transform.rotate(self.bug_img, 90)
        elif move == 'R':
            self.bugV += 1
            if self.bugV > 3:
                self.bugV = 0
            self.prev_view = self.last_view
            self.last_view = self.direction[self.bugV]
            self.bug_img = pygame.transform.rotate(self.bug_img, 270)

    # Agregar funciones de movimiento según las direcciones y lógica específica del juego
    def turn_left(self):
        self.bugV -= 1
        if self.bugV < 0:
            self.bugV = 3
        self.prev_view = self.last_view
        self.last_view = self.direction[self.bugV]
        self.movimientos.append(self.direction[self.bugV])
        self.all_movimientos.append('L')

    def turn_right(self):
        self.bugV += 1
        if self.bugV > 3:
            self.bugV = 0
        self.prev_view = self.last_view
        self.last_view = self.direction[self.bugV]
        self.movimientos.append(self.direction[self.bugV])
        self.all_movimientos.append('R')

    def move_up(self):
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

    def play(self):
        if not self.can_restart:
            self.move = 1
            self.pressed = True
            self.can_restart = True
            print(self.all_movimientos)

    def restart(self):
        self.cord_x = 625
        self.cord_y = 550
        self.dview = self.direction[3]
        while self.bug_view != self.dview:
            self.bugV -= 1
            if self.bugV < 0:
                self.bugV = 3
            self.bug_view = self.direction[self.bugV]
            self.bug_img = pygame.transform.rotate(self.bug_img, 90)
        self.last_view = self.direction[3]
        self.all_movimientos = []
        self.movimientos = []
        self.while_actions = []
        self.count_while = 0
        self.count_while2 = 0
        self.move = 0
        self.bugV = 3
        self.bugV2 = 3
        self.limit_x_min = 0
        self.limit_x_max = 1
        self.limit_y_min = 10
        self.limit_y_max = 11
        self.is_blocked()
        self.can_restart = False     
    
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

        move_wh = 0

        for move in range(len(self.all_movimientos)):
            if self.all_movimientos[move] in self.direction2:
                Move(move_cord_x,move_cord_y,self.up_mini_img,self.screen).draw()
            elif self.all_movimientos[move] == 'L':
                Move(move_cord_x,move_cord_y,self.turn_left_mini_img,self.screen).draw()
            elif self.all_movimientos[move] == 'R':
                Move(move_cord_x,move_cord_y,self.turn_right_mini_img,self.screen).draw()
            elif self.all_movimientos[move] == 'Wh':
                Move(move_cord_x, move_cord_y, self.while_mini_img, self.screen).draw()
                move_cord2_x = move_cord_x+30
                move_cord2_y = move_cord_y
                if self.while_actions:
                    for move2 in range(len(self.while_actions[move_wh])):
                        if  self.while_actions[move_wh][move2] == "L":
                            Move(move_cord2_x,move_cord2_y,self.turn_left_w_mini_img,self.screen).draw()
                        elif self.while_actions[move_wh][move2] == "R":
                            Move(move_cord2_x,move_cord2_y,self.turn_right_w_mini_img,self.screen).draw()
                        elif self.while_actions[move_wh][move2] == "M":
                            Move(move_cord2_x,move_cord2_y,self.up_mini_w_img,self.screen).draw()
                        elif self.while_actions[move_wh][move2] == "wall_on_left":
                            Move(move_cord2_x,move_cord2_y,self.wall_on_left_mini_img,self.screen).draw()
                        elif self.while_actions[move_wh][move2] == "wall_on_right":
                            Move(move_cord2_x,move_cord2_y,self.wall_on_right_mini_img,self.screen).draw()
                        elif self.while_actions[move_wh][move2] == "wall_in_front":
                            Move(move_cord2_x,move_cord2_y,self.wall_in_front_mini_img,self.screen).draw()

                        move_cord2_x += 30
                        if move_cord2_x > 500:
                            move_cord2_y += 30
                            move_cord2_x = 100

                move_wh += 1

                move_cord_x = move_cord2_x-30
                move_cord_y = move_cord2_y

            elif self.all_movimientos[move] == 'I':
                Move(move_cord_x, move_cord_y, self.if_mini_img, self.screen).draw()

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
        self.is_left_blocked()
        self.is_right_blocked()

    def is_left_blocked(self):
        if self.bug_view == 'E':
            self.left_limit = ((self.limit_x_min,self.limit_y_max),(self.limit_x_min,self.limit_y_min))
        if self.bug_view == 'S':
            self.left_limit = ((self.limit_x_max,self.limit_y_min),(self.limit_x_max,self.limit_y_max))
        if self.bug_view == 'W':
            self.left_limit = ((self.limit_x_min,self.limit_y_min),(self.limit_x_max,self.limit_y_min))
        if self.bug_view == 'N':
            self.left_limit = ((self.limit_x_min,self.limit_y_min),(self.limit_x_min,self.limit_y_max))

    def is_right_blocked(self):
        if self.bug_view == 'E':
            self.right_limit = ((self.limit_x_min,self.limit_y_min),(self.limit_x_max,self.limit_y_min))
        if self.bug_view == 'S':
            self.right_limit = ((self.limit_x_min,self.limit_y_min),(self.limit_x_min,self.limit_y_max))
        if self.bug_view == 'W':
            self.right_limit = ((self.limit_x_min,self.limit_y_max),(self.limit_x_min,self.limit_y_min))
        if self.bug_view == 'N':
            self.right_limit = ((self.limit_x_max,self.limit_y_min),(self.limit_x_max,self.limit_y_max))