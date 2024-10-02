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
    print(find_value_using_brute_force(8, [1,4,8,9,10,44], sum=56))
