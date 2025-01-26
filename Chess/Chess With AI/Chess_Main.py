"""
This is our main file responsible for handling user input and output.
"""
import pygame as py
import Chess_Engine

WIDTH = HEIGHT = 500 #400 is also a good option
DIMENSION = 8 #Chessboard are 8*8
SQ_SIZE = HEIGHT//DIMENSION
MAX_FPS = 15 #for animations later on
IMAGES = {}


#Initialize a global dictionary of images. This will be called exactly one time.

def load_images():
    pieces = ["wp", "wR", "wB", "wQ", "wK", "wN", "bp", "bR", "bB", "bQ", "bK", "bN"]
    for piece in pieces:
        IMAGES[piece] = py.transform.scale(py.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


#The main driver which will handle user input and update graphics.
def main():
    py.init()
    screen = py.display.set_mode((WIDTH, HEIGHT))
    clock = py.time.Clock()
    screen.fill(py.Color("white"))
    gs = Chess_Engine.GameState()
    load_images() #only once
    running = True
    sq_selected = () #no square selected, keep track of last click of user
    player_clicks = [] #keeps track of player clicks
    while running:
        for e in py.event.get():
            if e.type == py.QUIT:
                running = False
            elif e.type == py.MOUSEBUTTONDOWN:
                location  = py.mouse.get_pos() #(x, y) position of mouse
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sq_selected == (row, col):
                    sq_selected = () #deselects
                    player_clicks = [] #clear player click
                else:
                    sq_selected = (row, col)
                    player_clicks.append(sq_selected)
                if len(player_clicks) == 2: #after 2nd click
                    move = Chess_Engine.Move(player_clicks[0], player_clicks[1], gs.board)
                    gs.make_move(move)
                    sq_selected = () #resets the users clicks
                    player_clicks = []


        draw_game_state(screen, gs)
        clock.tick(MAX_FPS)
        py.display.flip()


#responsible for all graphics in the game state
def draw_game_state(screen, gs):
    draw_board(screen) #draw square on the board
    draw_pieces(screen, gs.board) #draw pieces on top of the square


#draw square on board. the top left square is light from both perspective.
def draw_board(screen):
    colors = [py.Color("white"), py.Color("grey")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r+c) % 2]
            py.draw.rect(screen, color, py.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE,SQ_SIZE))


#draw pieces on the top of square boxes
def draw_pieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], py.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE,SQ_SIZE))



if __name__ == "__main__":
    main()





















