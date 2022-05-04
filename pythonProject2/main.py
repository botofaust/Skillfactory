game_array = None
winner = None
empty_pole = '+'
player_pole = 'x'
comp_pole = 'o'
player_array = None
comp_array = None

def game_init():
    global game_array
    global winner
    global player_array
    global comp_array
    game_array = [[empty_pole, empty_pole, empty_pole],
                  [empty_pole, empty_pole, empty_pole],
                  [empty_pole, empty_pole, empty_pole]]
    player_array = [0,0,0, # rows
                    0,0,0, # cols
                    0,0]   # diags
    comp_array = [0,0,0, # rows
                  0,0,0, # cols
                  0,0]   # diags
    winner = None
    print('It has begun!')


def game_output_board():
    print('  1 2 3')
    for x in range(1, 4):
        print(f'{x} {game_array[x-1][0]} {game_array[x-1][1]} {game_array[x-1][2]}')


def game_question():
    answer = input('Do You want to play the GAME? [Y] ')
    return answer.lower == 'y' or answer == ''


def game_over():
    if winner is not None:
        print(f'{winner} is Winner!!')
        return True
    return False


def game_player_turn():
    while True:
        turn = list(map(int, input('?').split()))
        x, y = turn[0]-1, turn[1]-1
        if x not in range(0, 3) or y not in range(0, 3):
            print('bad coords!!')
        elif game_array[x][y] == empty_pole:
            game_array[x][y] = player_pole
            player_array[x] += 1
            player_array[y+3] += 1
            if x == y:
                player_array[6] += 1
            if x+y == 4:
                player_array[7] += 1
            return None
        else:
            print('bad turn')


def find_max(arr):
    tmp = enumerate(arr)
    return max(tmp, key=lambda i: i[1])


def comp_turn(x,y):
    game_array[x][y] = comp_pole
    comp_array[x] += 1
    comp_array[y + 3] += 1
    if x == y:
        comp_array[6] += 1
    if x + y == 4:
        comp_array[7] += 1


def game_comp_turn():
    row = find_max(comp_array + player_array)[0]
    if row > 7:
        row -= 8
    if row in range(0,3):
        while True:
            for i in range(0,3):
                if game_array[row][i] == empty_pole:
                    comp_turn(row, i)
                    return None
    if row in range(3,6):
        while True:
            for i in range(0,3):
                if game_array[i][row-3] == empty_pole:
                    comp_turn(i, row-3)
                    return None
    if row == 6:
        while True:
            for i in range(0,3):
                if game_array[i][i] == empty_pole:
                    comp_turn(i, i)
                    return None
    if row == 7:
        while True:
            for i in range(0,3):
                if game_array[i][3-i] == empty_pole:
                    comp_turn(row, i)
                    return None


def game_define_winner():
    win = winner
    max_in_row = find_max(player_array)
    if max_in_row[1] == 3:
        win = 'Player'
    max_in_row = find_max(comp_array)
    if max_in_row[1] == 3:
        win = 'Computer'
    return win


while game_question():
    game_init()
    game_output_board()
    while not game_over():
        game_player_turn()
        game_comp_turn()
        winner = game_define_winner()
        game_output_board()

