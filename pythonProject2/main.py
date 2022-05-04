game_array = None
winner = None
empty_pole = '+'
player_pole = 'x'
comp_pole = 'o'
player_array = None
comp_array = None
turns = 0

def game_init():
    global game_array
    global winner
    global player_array
    global comp_array
    global turns
    game_array = [[empty_pole, empty_pole, empty_pole],
                  [empty_pole, empty_pole, empty_pole],
                  [empty_pole, empty_pole, empty_pole]]
    player_array = [0, 0,      # diags
                    0, 0, 0,   # rows
                    0, 0, 0]   # cols
    comp_array = [0, 0,      # diags
                  0, 0, 0,   # rows
                  0, 0, 0]   # cols
    winner = None
    turns = 0
    print('It has begun!')


def game_output_board():
    print('  1 2 3')
    for x in range(1, 4):
        print(f'{x} {game_array[x-1][0]} {game_array[x-1][1]} {game_array[x-1][2]}')


def game_question():
    answer = input('Do You want to play the GAME? [Y] ')
    return answer.lower() == 'y' or answer == ''


def game_over():
    if winner is not None:
        print(f'{winner} is Winner!!')
        return True
    return False


def player_turn(x, y):
    global turns
    game_array[x][y] = player_pole
    player_array[x + 2] += 1
    player_array[y + 5] += 1
    if x == y:
        player_array[0] += 1
    if x + y == 2:
        player_array[1] += 1
    turns += 1


def game_player_turn():
    while True:
        turn = list(map(int, input('?').split()))
        x, y = turn[0]-1, turn[1]-1
        if x not in range(0, 3) or y not in range(0, 3):
            print('bad coords!!')
        elif game_array[x][y] == empty_pole:
            player_turn(x, y)
            return None
        else:
            print('bad turn')


def find_max(arr):
    tmp = enumerate(arr)
    return max(tmp, key=lambda i: i[1])


def comp_turn(x,y):
    global turns
    game_array[x][y] = comp_pole
    comp_array[x + 2] += 1
    comp_array[y + 5] += 1
    if x == y:
        comp_array[0] += 1
    if x + y == 2:
        comp_array[1] += 1
    turns += 1


def game_comp_turn():
    if game_array[1][1] == empty_pole:
        comp_turn(1, 1)
        return None
    row = find_max(comp_array)[0]
    turn = None
    if row in range(2, 5) and comp_array[row] + player_array[row] < 3:
        for i in range(0, 3):
            if game_array[row - 2][i] == empty_pole:
                turn = (row - 2, i)
    if row in range(5, 8) and comp_array[row] + player_array[row] < 3:
        for i in range(0, 3):
            if game_array[i][row-5] == empty_pole:
                turn = (i, row-5)
    if row == 0 and comp_array[row] + player_array[row] < 3:
        for i in range(0, 3):
            if game_array[i][i] == empty_pole:
                turn = (i, i)
    if row == 1 and comp_array[row] + player_array[row] < 3:
        for i in range(0, 3):
            if game_array[i][2 - i] == empty_pole:
                turn = (i, 2 - i)
    if comp_array[row] == 2 and turn is not None:
        # one step to WIN!
        comp_turn(turn[0], turn[1])
        return None

    row = find_max(player_array)[0]
    if row in range(2, 5) and comp_array[row] + player_array[row] < 3:
        for i in range(0, 3):
            if game_array[row - 2][i] == empty_pole:
                turn = (row - 2, i)
    if row in range(5, 8) and comp_array[row] + player_array[row] < 3:
        for i in range(0, 3):
            if game_array[i][row - 5] == empty_pole:
                turn = (i, row - 5)
    if row == 0 and comp_array[row] + player_array[row] < 3:
        for i in range(0, 3):
            if game_array[i][i] == empty_pole:
                turn = (i, i)
    if row == 1 and comp_array[row] + player_array[row] < 3:
        for i in range(0, 3):
            if game_array[i][2 - i] == empty_pole:
                turn = (i, 2 - i)
    if turn is None:
        for x in range(0, 3):
            for y in range(0, 3):
                if game_array[x][y] == empty_pole:
                    turn = (x, y)
                    break
    comp_turn(turn[0], turn[1])


def game_define_winner():
    win = winner
    max_in_row = find_max(player_array)
    if max_in_row[1] == 3:
        win = 'Player'
    max_in_row = find_max(comp_array)
    if max_in_row[1] == 3:
        win = 'Computer'
    if turns == 9:
        win = 'Friendship'
    return win


while game_question():
    game_init()
    game_output_board()
    while not game_over():
        game_player_turn()
        winner = game_define_winner()
        if winner is None:
            game_comp_turn()
            winner = game_define_winner()
        game_output_board()

