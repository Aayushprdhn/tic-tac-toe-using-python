import random
import os.path
import json
random.seed()

def draw_board(board):
    '''Prints a visual representation of the board with lines and cells'''
    print("-------------")
    for row in board:
        print("|", end="")
        for cell in row:
            print(" " + cell + " |", end="")
        print("\n-------------")

def welcome(board):
    '''Displays a welcome message and show the initial board layout,
    helps the player understand the cell positions (1-9)'''
    print('Welcome to the "unbeateable Noughts and Crosses" game.')
    print("The board layout is show below:\n",)
    draw_board(board)

def initialise_board(board):
    '''Reset the board to empty spaces.'''
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
    return board

def get_player_move(board):
    '''Asks the player to choose a move (1-9) and validate it.'''
    while True:
        try:
            move = int(input("Enter your move (1-9):")) - 1
            row, col = divmod(move, 3)
            if 0 <= move <= 8 and board[row] [col] == ' ':
                return row, col
            else:
                print("Invalid move. Cell occupied or out of range.")
        except ValueError:
            print("Please enter a number between 1-9.")
    return row, col

def choose_computer_move(board):
    '''Let the computer choose an empty cell'''
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    row, col = random.choice(empty_cells)
    return row, col

def check_for_win(board, mark):
    '''Check if a player has won the game.'''
    win_pattern = [
        [[0, 0], [0, 1], [0, 2]], 
        [[1, 0], [1, 1], [1, 2]], 
        [[2, 0], [2, 1], [2, 2]], 
        [[0, 0], [1, 0], [2, 0]], 
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]], 
        [[0, 0], [1, 1], [2, 2]],
        [[0, 2], [1, 1], [2, 0]], 
    ]

    for pattern in win_pattern:
        if all(board[r][c] == mark for r, c in pattern):
            return True
    return False

def check_for_draw(board):
    '''Checks if the game is a draw (all cells filled, no winner)'''
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True
        
def play_game(board):
    '''PLay one full game of Tic-Tac-Toe.'''
    initialise_board(board)
    draw_board(board)
    while True:
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)
        if check_for_win(board, 'X'):
            return 1
        if check_for_draw(board):
            return 0
        
        row, col = choose_computer_move(board)
        board[row][col] = 'O'
        draw_board(board)
        if check_for_win(board, 'O'):
            return -1
        if check_for_draw(board):
            return 0
    return 0       
                
def menu():
    '''Displays the game menu and get the player's choice.'''
    print("Menu:")
    print("1 - Play the game")
    print("2 - Save scores in the file 'leaderboard.txt'")
    print("3 - Load and display the scores form 'leaderboard.txt'")
    print("q - End the program")
    choice = input("Enter your choice: ")
    while choice not in ['1', '2', '3', 'q']:
        choice = input("Invalid choice. Enter 1, 2, 3 or q: ")
    return choice

def load_scores():
    '''Load scores from 'leaderboard.txt' '''
    leaders = {}
    if os.path.exists("leaderboard.txt"):
        with open("leaderboard.txt", "r") as f:
            for line in f:
                name, score = line.strip().split(":")
                leaders[name] = int(score)
    return leaders
    
def save_score(score):
    '''Save the score to 'leaderboard.txt' asks the player for their name'''
    while True:
        name = input("Enter your name: ").strip()
        if name:
            break
        else:
            print("Name cannot be empty. Please enter valid name.")

    with open("leaderboard.txt", "a") as f:
        f.write(f"{name}:{score}\n")
    return

def display_leaderboard(leaders):
    '''Display's each player name and scores'''
    print("Leaderboard:")
    if not leaders:
        print("No scores yet.")
    else:
        for name, score in leaders.items():
            print(f"{name}:{score}")