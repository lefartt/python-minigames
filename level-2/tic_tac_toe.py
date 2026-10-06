import random


def display_board(board):
    print("\n")
    print("     |     |")
    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}")
    print("_____|_____|_____")
    print("     |     |")
    print(f"  {board[3]}  |  {board[4]}  |  {board[5]}")
    print("_____|_____|_____")
    print("     |     |")
    print(f"  {board[6]}  |  {board[7]}  |  {board[8]}")
    print("     |     |")
    print()


def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combination in winning_combinations:
        if all(board[position] == player for position in combination):
            return True

    return False


def board_full(board):
    return all(position in ["X", "O"] for position in board)


def get_player_move(board):
    while True:
        choice = input("Choose a position (1-9): ")

        if not choice.isdigit():
            print("Please enter a number from 1 to 9.")
            continue

        position = int(choice)

        if position < 1 or position > 9:
            print("Please choose a number from 1 to 9.")
            continue

        index = position - 1

        if board[index] in ["X", "O"]:
            print("That position is already taken.")
            continue

        return index


def get_ai_move(board):
    available_positions = []

    for index in range(len(board)):
        if board[index] not in ["X", "O"]:
            available_positions.append(index)

    return random.choice(available_positions)


def play_game(game_mode):
    board = [
        "1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"
    ]

    current_player = "X"

    while True:

        display_board(board)

        # Player vs AI
        if game_mode == "ai" and current_player == "O":

            print("AI is thinking...")

            index = get_ai_move(board)

            board[index] = "O"

            print(f"AI chose position {index + 1}.")

        else:

            if game_mode == "ai":
                print("Your turn!")

            else:
                print(f"Player {current_player}'s turn.")

            index = get_player_move(board)

            board[index] = current_player

        # Check winner
        if check_winner(board, current_player):
            display_board(board)

            if game_mode == "ai" and current_player == "O":
                print("AI wins!")

            else:
                print(f"Player {current_player} wins!")

            break

        # Check draw
        if board_full(board):
            display_board(board)
            print("It's a draw!")
            break

        # Switch player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


while True:

    print("\n========== TIC-TAC-TOE ==========")

    print("\nChoose game mode:")
    print("1. Player vs Player")
    print("2. Player vs AI")

    while True:
        mode = input("\nChoose an option (1-2): ")

        if mode == "1":
            game_mode = "pvp"
            break

        elif mode == "2":
            game_mode = "ai"
            break

        else:
            print("Invalid choice. Please choose 1 or 2.")

    if game_mode == "pvp":
        print("\nPlayer X vs Player O")

    else:
        print("\nYou are X.")
        print("AI is O.")

    play_game(game_mode)

    while True:
        replay = input("\nPlay again? (y/n): ").lower()

        if replay == "y":
            break

        elif replay == "n":
            print("\nThanks for playing Tic-Tac-Toe!")
            print("Goodbye!")
            exit()

        else:
            print("Invalid choice. Please enter 'y' or 'n'.")
