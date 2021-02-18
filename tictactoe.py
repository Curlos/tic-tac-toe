from random import choice


def player_turn(board, squares, all_pos, player_num, all_winning_pos):
    ''' Asks the player to enter a valid, empty square and adds it to the board. '''
    while True:
        print(board)
        player_square = input(
            f"Player {player_num}'s turn.\nEnter square: (e.g. A0): ")

        if player_square in squares.keys():
            if squares[player_square] == ' ':
                if player_num == '1':
                    squares[player_square] = 'X'
                    all_pos.append(player_square)
                    return check_all_pos(all_winning_pos, all_pos, 'X')
                else:
                    squares[player_square] = 'O'
                    all_pos.append(player_square)
                    return check_all_pos(all_winning_pos, all_pos, 'O')
                break
            else:
                print('Square already full. Please enter an empty one.')
        else:
            print(
                'Square invalid, please enter a valid, empty square from the following list: [A0, A1, A2, B0, B1, B2, C0, C1, C2]')


def ai_turn(board, squares, all_pos, all_winning_pos):
    ''' Asks the player to enter a valid, empty square and adds it to the board. '''
    print(board)
    ai_square = choice(list(squares.keys()))

    while True:
        if squares[ai_square] != ' ':
            ai_square = choice(list(squares.keys()))
        else:
            break
    squares[ai_square] = 'O'
    all_pos.append(ai_square)
    return check_all_pos(all_winning_pos, all_pos, 'O')


def check_all_pos(all_winning_pos, all_pos, letter):
    ''' Checks if there are either three X's or three O's in a row on the board. If there are then the game would finish, otherwise it continues '''
    print(f"Checking all positions of {letter}: {all_pos}")
    for winning_pos in all_winning_pos:
        check = all(item in all_pos for item in winning_pos)

        if(check):
            print(f"Crossed the 3 squares: {winning_pos}")
            return True
    return False


def update_board(board, squares):
    ''' Updates the printed board. Does not affect the logic of the board in the dictionary. '''
    board = f'    A    B     C\n'
    board += f"0 | {squares['A0'].center(2)} | {squares['B0'].center(2)} | {squares['C0'].center(2)} |\n"
    board += f"1 | {squares['A1'].center(2)} | {squares['B1'].center(2)} | {squares['C1'].center(2)} |\n"
    board += f"2 | {squares['A2'].center(2)} | {squares['B2'].center(2)} | {squares['C2'].center(2)} |\n"

    return board


def start():
    ''' Starts the game '''
    running = True
    squares = {'A0': ' ', 'A1': ' ', 'A2': ' ', 'B0': ' ',
               'B1': ' ', 'B2': ' ', 'C0': ' ', 'C1': ' ', 'C2': ' '}

    all_x_pos = []
    all_o_pos = []

    board = f'    A    B     C\n'
    board += f"0 | {squares['A0'].center(2)} | {squares['B0'].center(2)} | {squares['C0'].center(2)} |\n"
    board += f"1 | {squares['A1'].center(2)} | {squares['B1'].center(2)} | {squares['C1'].center(2)} |\n"
    board += f"2 | {squares['A2'].center(2)} | {squares['B2'].center(2)} | {squares['C2'].center(2)} |\n"

    all_winning_pos = []

    all_winning_pos.append(['A0', 'B0', 'C0'])
    all_winning_pos.append(['A0', 'B1', 'C2'])
    all_winning_pos.append(['A0', 'A1', 'A2'])

    all_winning_pos.append(['A1', 'B1', 'C1'])
    all_winning_pos.append(['B0', 'B1', 'B2'])
    all_winning_pos.append(['C0', 'C1', 'C2'])

    all_winning_pos.append(['A2', 'B2', 'C2'])
    all_winning_pos.append(['A2', 'B1', 'C0'])

    game_type = input(
            "Choose a game mode [Enter '1' or '2']:\n1. Player vs. Player\n2. Player vs. AI\n")

    while running:
        player_one = player_turn(
            board, squares, all_x_pos, '1', all_winning_pos)
        board = update_board(board, squares)

        # Returns true if the player has placed three X in positions where it can be crossed
        if(player_one):
            print(board)
            print(f"Game over! Player one has won the game!")
            break

        print(len(all_x_pos) + len(all_o_pos))

        if(game_type == '1'):
            player_two = player_turn(
                board, squares, all_o_pos, '2', all_winning_pos)
            board = update_board(board, squares)

            # Returns true if the player has placed three X in positions where it can be crossed
            if(player_two):
                print(board)
                print(f"Game over! Player two has won the game!")
                break
        elif(game_type == '2'):
            player_ai = ai_turn(
                board, squares, all_o_pos, all_winning_pos)
            board = update_board(board, squares)

            if(player_ai):
                print(board)
                print(f"Game over! Player AI has won the game!")
                break
        else:
            print('Invalid game mode entered. Please try again.')


def main():
    ''' Main '''
    start()


main()
