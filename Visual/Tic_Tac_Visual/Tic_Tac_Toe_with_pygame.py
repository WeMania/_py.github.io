import pygame, os, time

pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("                   Tic_Tac_Toe")
clock = pygame.time.Clock()
font = pygame.font.Font("assets/Pixeltype.ttf", 80)
full_screen = pygame.image.load("assets/background.png").convert_alpha()
screen_fill = pygame.Surface((600, 600))
screen_fill.fill("#e56565")

x_sur = pygame.image.load("assets/X.png").convert_alpha()
o_sur = pygame.image.load("assets/O.png").convert_alpha()
marvel = x_sur
move_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
move = "x"
game_on = True

rec_list = [marvel.get_rect(topleft = (50,50)),
			marvel.get_rect(topleft = (250,50)),
			marvel.get_rect(topleft = (450,50)),
			marvel.get_rect(topleft = (50,250)),
			marvel.get_rect(topleft = (250,250)),
			marvel.get_rect(topleft = (450,250)),
			marvel.get_rect(topleft = (50,450)),
			marvel.get_rect(topleft = (250,450)),
			marvel.get_rect(topleft = (450,450))]


def interface():
	screen.blit(full_screen, (0,0))
	screen.blit(screen_fill, (50,50))
	pygame.draw.line(screen, "#0b2c3f", (250,50), (250,650), 3)
	pygame.draw.line(screen, "#0b2c3f", (450,50), (450,650), 3)
	pygame.draw.line(screen, "#0b2c3f", (50,250), (650,250), 3)
	pygame.draw.line(screen, "#0b2c3f", (50,450), (650,450), 3)
	game_over_fun()


def game_over_fun():
	global display_restart_rec
	display_restart = font.render(f"> Restart <", True, "black")
	display_restart_rec = display_restart.get_rect(center = (350, 680))
	screen.blit(display_restart, display_restart_rec)


def winner_fun():
	global game_on
	dysplay_game_over = font.render(f"{winner} Won The Game !", True, "red")
	screen.blit(dysplay_game_over, (160,0))
	game_on = False


def winner_finder(a, b , c):
	global winner
	if a == b and b == c and c != 0:
		winner = a
		return winner_fun()


interface()
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	if pygame.mouse.get_pressed()[0]:
		if display_restart_rec.collidepoint(pygame.mouse.get_pos()):
			interface()
			marvel = x_sur
			move_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
			move = "x"
			game_on = True
			time.sleep(0.1)

	if move_list.count("x") == 5 and game_on: 
		dysplay_game_over = font.render(f"Its A Draw ! ", True, "red")
		screen.blit(dysplay_game_over, (200,0))
		game_on = False

	if pygame.mouse.get_pressed()[0]:
		for i, s in enumerate(rec_list):
			if s.collidepoint(pygame.mouse.get_pos()) and move_list[i] == 0 and game_on:
				screen.blit(marvel, s)
				move_list[i] = move
				marvel = o_sur if move == "x" else x_sur
				move = "x" if move == "o" else "o"

	winner_finder(move_list[0], move_list[1], move_list[2])
	winner_finder(move_list[3], move_list[4], move_list[5])
	winner_finder(move_list[6], move_list[7], move_list[8])
	winner_finder(move_list[0], move_list[3], move_list[6])
	winner_finder(move_list[1], move_list[4], move_list[7])
	winner_finder(move_list[2], move_list[5], move_list[8])
	winner_finder(move_list[0], move_list[4], move_list[8])
	winner_finder(move_list[2], move_list[4], move_list[6])

	pygame.display.update()
	clock.tick(60)