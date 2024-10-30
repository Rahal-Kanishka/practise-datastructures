from enum import Enum


def find_max_profits(price_array):
    # this will be O(n^2) time complexity solution , space complexity 1 (because just two variables)
    max_profit = price_array[1] - price_array[0]
    max_index = [-1] * 2
    i = 0
    j = 1
    while i < len(price_array) - 1:
        j = i + 1
        while j < len(price_array):
            if (price_array[j] - price_array[i]) > max_profit:
                max_profit = price_array[j] - price_array[i]
                max_index = [i, j]
                print('max_profit = ', max_profit, ', max_index = ', max_index)
            j += 1
        i += 1
    return max_profit, max_index


def find_id_peak(array):
    i = 1
    while i < len(array) - 1:
        if array[i - 1] < array[i] > array[i + 1]:
            return i
        i += 1
    return -1


def column(matrix, i):
    return [row[i] for row in matrix]


def find_peak_in_matrix(matrix):
    # find peak in where the dip is same in a crossing row and a column
    print('len: ', len(matrix))
    a = 0
    b = 0
    peaks = []
    while a < len(matrix):
        row_peak = (find_id_peak(matrix[a]))
        while row_peak != -1 and b < len(matrix):
            print('row_peak = ', row_peak, ',a: ', a)
            column_peak = find_id_peak(column(matrix, b))
            print('column_peak = ', column_peak, ',b: ', b)
            if a == column_peak:
                peaks.append([a, b])
                break
            b += 1
        a += 1
    return peaks


# chessboard is 8 X 8, if place the queen on the first square (0,0)
# only queen can be for a one row, same goes to a column.
# According to the question of where queens are not allowed to see each other,
# therefore maximum queens can be placed should be 8
# starting from 0,0
def place_queen_in_chessboard(matrix):
    colum_dic = {}  # keep track of columns used
    count = 0
    position_array = []
    # count += 1
    # colum_dic[0] = 0
    # first piece placed
    i = 0
    j = 0
    # last row shouldn't have a queen, since all position are already occupied
    while i < len(matrix) - 1:
        while j < len(matrix):
            if j not in colum_dic.keys():
                position_array.append([i, j])
                colum_dic[j] = j
                count += 1
                if j + 2 >= len(matrix):
                    j = 0
                elif j + 2 < len(matrix):
                    j += 2
                # since no queen can go in the same row
                break
            else:
                j += 1
        i += 1
    return position_array, count


def find_value_using_brute_force(size, array, sum):
    i = 0
    j = 0
    k = 0
    result = []
    while i < len(array):
        j = i + 1
        while j < len(array):
            k = j + 1
            while k < len(array):
                if array[i] + array[j] + array[k] == sum:
                    result.append([array[i], array[j], array[k]])
                k += 1
            j += 1
        i += 1
    return result


# class syntax

class Mark(Enum):
    Friendly = 1
    Opposition = -1


def play_TicTacToe(opposition_play_x, opposition_play_y, board):
    # program plays 1
    # enemy plays -1

    board[opposition_play_x][opposition_play_y] = Mark.Opposition.value
    print('board: ', board)
    cell_count = 0
    highest_win_points = 0
    highest_def_points = 0
    def_points, win_points = 0, 0
    def_location, win_location = 0, 0
    final_play_location = None
    final_points = 0

    for row_index, row in enumerate(board):
        for cell_index, cell in enumerate(row):
            print('cell: ', cell_count, ' value: ', cell)
            # print win, def values where not yet played cells
            if cell is not Mark.Friendly.value and cell is not Mark.Opposition.value:
                cell_win_points, cell_def_points = 0, 0
                cell_def_points += count_def_point(row_index, cell_index, board)
                cell_win_points += count_win_points(row_index, cell_index, board)

                # check is the point in diagonal
                if row_index == cell_index:
                    print('point is in main diagonal')
                    def_points, win_points = check_upwards_diagonal(board)
                    cell_win_points += win_points
                    cell_def_points += def_points
                if row_index == 0 and cell_index == (len(board) - 1) or (
                        row_index == len(board) - 1 and cell_index == 0) or (row_index == 1 and cell_index == 1):
                    print('point is diagonal: ', row_index, cell_index)
                    def_points_upwards, win_points_upwards = check_downward_diagonal(board)
                    cell_win_points += win_points_upwards
                    cell_def_points += def_points_upwards
                if cell_def_points > highest_def_points:
                    highest_def_points = cell_def_points
                    def_location = [row_index, cell_index]
                if cell_win_points > highest_win_points:
                    highest_win_points = cell_win_points
                    win_location = [row_index, cell_index]
                print('win points: ', cell_win_points, ' def points: ', cell_def_points)
            cell_count += 1

    if highest_win_points > highest_def_points:
        print('going to play to win')
        final_play_location = win_location
        final_points = highest_win_points
    else:
        print('going to play defensive')
        final_play_location = def_location
        final_points = highest_def_points

    return final_play_location, final_points


def count_win_points(x, y, board):
    row = board[x]
    points = 0
    i = len(board) - 1

    if row.count(Mark.Opposition.value) == 0:
        # means enemy have no pieces in the row
        points += 1

    # check urgent to win the row
    if row.count(Mark.Friendly.value) == 2:
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
        points += 1

    return points


def count_def_point(x, y, board):
    points = 0
    row = board[x]
    # row
    if row.count(Mark.Opposition.value) > 0:
        points += 1
    # in urgent matter
    if row.count(Mark.Friendly.value) == 2:
        points += 1

    # column
    i = len(board) - 1
    column_found = False
    opposition_count = 0
    while not column_found and i >= 0:
        if board[i][y] == Mark.Opposition.value:
            points += 1
        if board[i][y] == Mark.Opposition.value:
            opposition_count += 1
        i -= 1
    if opposition_count == 2:
        points += 1
    return points


def check_diagonal_points(board):
    opposition_count = 0
    friendly_count = 0
    down_opposition_count = 0
    down_friendly_count = 0
    points = 0
    def_points = 0
    # right to left diagonal, upwards
    def_points, points = check_upwards_diagonal(board)

    down_def_points, down_win_points = check_downward_diagonal(board)

    return (points + down_win_points), (def_points + down_win_points)


def check_downward_diagonal(board):
    def_points, down_friendly_count, down_opposition_count, points = 0, 0, 0, 0
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
    # URGENT scenario
    if down_friendly_count == 2:
        points += 1
    return def_points, points


def check_upwards_diagonal(board):
    def_points, friendly_count, opposition_count, points = 0, 0, 0, 0
    i = len(board) - 1
    j = len(board[0]) - 1
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
    # URGENT scenario
    if friendly_count == 2:
        points += 1
    return def_points, points


def count_win_point_diagonal(x, y, board):
    # check if x,y belong to diagonal. if not return 0 for both
    if x == y or (x == 0 and y == (len(board) - 1)) or (x == len(board) - 1 and y == 0):
        return 1
    else:
        return 0


if __name__ == '__main__':
    # print(find_max_profits([35, 45, 6, 10, 22, 11, 80]))
    # print(find_id_peak([1, 0, 0, 0, 0, 0, 1]))

    A = [[1, 2, 3, 4],  # 0
         [5, 6, 7, 8],  # 1
         [2, 20, 12, 8],  # 2
         [25, 2, 30, 8],  # 3
         [25, 16, 6, 8],  # 4
         ]
    # print(find_peak_in_matrix(A))

    rows, cols = (8, 8)
    arr = [[0] * cols] * rows
    # print(place_queen_in_chessboard(arr))
    # print(find_value_using_brute_force(8, [1,4,8,9,10,44], sum=56))
    board = [[0] * 3 for i in range(3)]
    location, points = play_TicTacToe(1, 1, board)
    print('computer plays on ', location, ' for ', points, ' points')
