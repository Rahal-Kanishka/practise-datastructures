from enum import Enum


class Mark(Enum):
    Friendly = 1
    Opposition = -1


def play_TicTacToe(board):
    # program plays 1
    # enemy plays -1

    # board[opposition_play_x][opposition_play_y] = Mark.Opposition.value
    print('board: ', board)
    cell_count = 0
    highest_win_points = 0
    highest_def_points = 0
    def_points, win_points = 0, 0
    def_location, win_location = 0, 0
    final_play_location = None
    final_points = 0
    win_flag = False

    for row_index, row in enumerate(board):
        for cell_index, cell in enumerate(row):
            print('cell: ', cell_count, ' value: ', cell)
            # print win, def values where not yet played cells
            if cell is not Mark.Friendly.value and cell is not Mark.Opposition.value:
                cell_win_points, cell_def_points = 0, 0
                cell_def_points += count_def_point(row_index, cell_index, board)
                row_column_win_points, win_flag = count_win_points(row_index, cell_index, board)
                cell_win_points += row_column_win_points

                # check is the point in diagonal
                if row_index == cell_index:
                    def_points, win_points, win_flag = check_right_bottom_to_top_diagonal(board)
                    print('point is in main diagonal: def_points: ', def_points, ' win_points: ', win_points)
                    cell_win_points += win_points
                    cell_def_points += def_points
                if row_index == 0 and cell_index == (len(board) - 1) or (
                        row_index == len(board) - 1 and cell_index == 0) or (row_index == 1 and cell_index == 1):
                    print('point is diagonal: ', row_index, cell_index)
                    def_points_upwards, win_points_upwards, win_flag = check_downward_diagonal(board)
                    cell_win_points += win_points_upwards
                    cell_def_points += def_points_upwards

                if win_flag:
                    win_location = [row_index, cell_index]
                    break
                if cell_def_points > highest_def_points:
                    highest_def_points = cell_def_points
                    def_location = [row_index, cell_index]
                if cell_win_points > highest_win_points:
                    highest_win_points = cell_win_points
                    win_location = [row_index, cell_index]
                print('win points: ', cell_win_points, ' def points: ', cell_def_points)
            cell_count += 1

    if win_flag:
        print('win flag detected: ', win_location)
        final_play_location = win_location
        final_points = highest_win_points
    elif highest_win_points > highest_def_points:
        print('going to play to win')
        final_play_location = win_location
        final_points = highest_win_points
    else:
        print('going to play defensive')
        final_play_location = def_location
        final_points = highest_def_points

    return final_play_location, final_points


def count_win_points(x, y, board):
    win_flag = False
    row = board[x]
    points = 0
    i = len(board) - 1

    if row.count(Mark.Opposition.value) == 0:
        # means enemy have no pieces in the row
        points += 1

    # check urgent to win the row
    if row.count(Mark.Friendly.value) == 2:
        win_flag = True
        points += 1

    column_found = False  # makes True if enemy mark found
    friendly_count = 0
    while not column_found and i >= 0:
        if board[i][y] == Mark.Opposition.value:
            column_found = True
        if board[i][y] == Mark.Friendly.value:
            friendly_count += 1
        i -= 1

    if not column_found:
        # no enemy presence in the column
        points += 1
    # check if there is urgent win for the column
    if friendly_count == 2:
        win_flag = True
        points += 1

    return points, win_flag


def count_def_point(x, y, board):
    points = 0
    row = board[x]
    # row
    if row.count(Mark.Opposition.value) > 0:
        points += 1
    # in urgent matter
    if row.count(Mark.Opposition.value) == 2:
        points += 1

    # column
    i = len(board) - 1
    column_found = False
    opposition_count = 0
    while not column_found and i >= 0:
        if board[i][y] == Mark.Opposition.value:
            points += 1
            opposition_count += 1
        i -= 1
    if opposition_count == 2:
        points += 1
    return points


def check_downward_diagonal(board):
    def_points, down_friendly_count, down_opposition_count, points = 0, 0, 0, 0
    win_flag = False
    # right to left diagonal, downwards
    i = 0
    j = len(board[0]) - 1
    while i < len(board) and j >= 0:
        if board[i][j] == Mark.Opposition.value:
            down_opposition_count += 1
        if board[i][j] == Mark.Friendly.value:
            down_friendly_count += 1
        i += 1
        j -= 1
    if down_opposition_count == 0:
        points += 1
    if down_opposition_count > 0:
        def_points += 1
    # Urgent scenario to def
    if down_opposition_count == 2:
        def_points += 1
    # URGENT scenario to win
    if down_friendly_count == 2:
        points += 1
        win_flag = True
    return def_points, points, win_flag


def check_right_bottom_to_top_diagonal(board):
    def_points, friendly_count, opposition_count, points = 0, 0, 0, 0
    i = len(board) - 1
    j = len(board[0]) - 1
    win_flag = False
    while i >= 0 and j >= 0:
        if board[i][j] == Mark.Opposition.value:
            opposition_count += 1
        if board[i][j] == Mark.Friendly.value:
            friendly_count += 1
        i -= 1
        j -= 1
    if opposition_count == 0:
        points += 1
    if opposition_count > 0:
        def_points += 1
    # Urgent scenario to def
    if opposition_count == 2:
        def_points += 1
    # URGENT scenario to win
    if friendly_count == 2:
        points += 1
        win_flag = True
    return def_points, points, win_flag


if __name__ == '__main__':
    board = [[0] * 3 for i in range(3)]
    exit_game = False
    while not exit_game:
        exit_input = input("Do you want to exit,y/N?")
        if exit_input == 'y' or exit_input == 'Y':
            exit_game = True
            continue
        x_input = input("enter row (0 index base)")
        y_input = input("enter column (0 index base)")
        board[int(x_input)][int(y_input)] = Mark.Opposition.value
        location, points = play_TicTacToe(board)
        print('computer plays on ', location, ' for ', points, ' points')
        board[location[0]][location[1]] = Mark.Friendly.value