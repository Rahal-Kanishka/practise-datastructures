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


if __name__ == '__main__':
    # print(find_max_profits([35, 45, 6, 10, 22, 11, 80]))
    # print(find_id_peak([1, 0, 0, 0, 0, 0, 1]))

    A = [[1, 2, 3, 4], #0
         [5, 6, 7, 8], #1
         [2, 20, 12, 8],#2
         [25, 2, 30, 8],#3
         [25, 16, 6, 8],#4
         ]
    print(find_peak_in_matrix(A))
