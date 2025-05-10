def print_board(board):
    print("\n")
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))
    print("\n")

def check_win(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # columns
        [0,4,8], [2,4,6]           # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_draw(board):
    return all(space != ' ' for space in board)

def get_player_move(player, board):
    while True:
        try:
            move = input(f"Player {player}, enter your move (1-9): ")
            if move.lower() == 'q':
                print("Game exited.")
                exit()
            move = int(move)
            if move < 1 or move > 9:
                print("Invalid input. Please enter a number from 1 to 9.")
                continue
            if board[move-1] != ' ':
                print("That spot is already taken. Try again.")
                continue
            return move - 1
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 9, or q to quit.")

def main():
    print("Welcome to Tic Tac Toe!")
    print("Enter numbers 1-9 to place your mark as shown below:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print("Enter 'q' anytime to quit.\n")

    while True:
        board = [' '] * 9
        current_player = 'X'
        game_over = False

        while not game_over:
            print_board(board)
            move = get_player_move(current_player, board)
            board[move] = current_player

            if check_win(board, current_player):
                print_board(board)
                print(f"Congratulations! Player {current_player} wins!")
                game_over = True
            elif check_draw(board):
                print_board(board)
                print("It's a draw!")
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'

        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()

