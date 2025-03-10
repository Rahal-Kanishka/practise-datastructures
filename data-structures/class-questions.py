from enum import Enum

import random
import math


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
    # print(find_value_using_brute_force(8, [1,4,8,9,10,44], sum=56))


def calculate_pie_values():
    initial_train = 10000000
    trials = initial_train
    hit = 0

    while trials >= 0:
        # throw dart randomly
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        # print(x,y , 'x,y')
        # check if the dart falls into the circle
        distance = abs(math.sqrt(((x - 0.5) * (x - 0.5)) + ((y - 0.5) * (y - 0.5))))
        if distance <= 0.5:
            hit += 1
        trials -= 1
        print('hits: ', hit)
    return 4 * (hit / initial_train)


def findLongestNonDecreasing_subsequence(arr):
    # every two adjacent elements the bigger number is at least twice the smaller one
    max_subsequence = []
    max_length = 0
    subsequence = []  # start of arra, end of array
    subsequence_length = 0
    # using brute force
    for i in range(len(arr) - 1):
        if arr[i + 1] >= (arr[i] * 2):
            subsequence.append(i)
            subsequence_length += 1
        elif i > 1 and arr[i] >= (arr[i - 1] * 2):
            subsequence.append(i)
            subsequence_length += 1
            if subsequence_length > max_length:
                max_subsequence = subsequence
                max_length = subsequence_length
            # clearing sequence since next element is not qualified, only the previous element is qualified
            subsequence = []
            subsequence_length = 0
        elif subsequence_length > max_length:
            max_subsequence = subsequence
            max_length = subsequence_length
            subsequence = []
            subsequence_length = 0
            # erase subsequence array
        print(i, arr[i], arr[i + 1], subsequence, max_subsequence)

    # last check before loop exit
    if subsequence_length > max_length:
        max_subsequence = subsequence
        max_length = subsequence_length
        subsequence = []
        subsequence_length = 0
    return max_subsequence


class DynamicStack:
    def __init__(self):
        self.items = []
        self.maxLength = 100
        self.top = 0
        self.rear = 0

    def push(self, value):
        if len(self.items) == self.maxLength:
            self.maxLength += self.maxLength
        self.items.append(value)
        self.top += 1

    def pop(self):
        if self.top > 1:
            self.top -= 1
            return self.items.pop()
        else:
            return -1

    def peek(self):
        return self.items[self.top-1]

    def __str__(self):
        return "top: " + str(self.peek()) + " length: " + str(len(self.items)) + ", maxLength: " + str(self.maxLength)


class DynamicCircularQueue:
    # using front and rear pointers to avoid shift all elements when add remove items
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.count = 0
        self.maxSize = 5
        self.items = [None] * self.maxSize  # Preallocate space

    def resize(self):
        print("Resizing the array...")
        new_size = self.maxSize * 2  # Double the size
        new_items = [None] * new_size  # New larger array

        # Copy elements to the new array in proper order
        for i in range(self.count):
            new_items[i] = self.items[(self.front + i) % self.maxSize]

        # Update references
        self.items = new_items
        self.front = 0
        self.rear = self.count-1
        self.maxSize = new_size
        print(self)

    def enqueue(self, item):
        if self.isFull():
            # if full extend the array
            self.resize()
            # check the rear is at the end an
        elif self.rear == self.maxSize:
            # since array is not empty and the rear is at the end, insert it to the front
            self.rear = 0
        if self.isEmpty():
            self.items[0] = item
            self.rear += 1
            self.front += 1
            self.count += 1
            return
        # else:

        self.count += 1
        # after inserting item evaluate rear
        if self.rear >= self.maxSize-1:
            self.rear = 0
        else:
            self.rear += 1
        self.items[self.rear] = item

    def dequeue(self):
        if self.isEmpty():
            return Exception("Queue is empty")
        else:
            result = self.items[self.front]
            self.items[self.front] = None
        if self.front == self.maxSize:
            self.front = 0
        else:
            self.front += 1
        self.count -= 1
        return result

    def peek(self):
        return self.items[self.front]

    def isFull(self):
        return self.count == self.maxSize

    def isEmpty(self):
        return self.count == 0

    def __str__(self):
        return (str(self.items) + " count: " + str(self.count) + " ,front: " + str(self.front)
                + ", rear: " + str(self.rear) + ", maxSize: " + str(self.maxSize))


class MaxHeap:
    def __init__(self, size=100):
        self.size = size
        self.heap = []

    def build_from_array(self, arr):
        # Sorts the array and inserts one element at a time
        sorted_arr = sorted(arr, reverse=True)  # Sort array in descending order
        self.heap = []  # Clear the heap
        for element in sorted_arr:
            self.insert(element)

    def insert(self, val):
        """Inserts a new integer into the heap."""
        if len(self.heap) >= self.size:
            raise Exception("Heap is full")
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def max(self):
        if not self.heap:
            raise Exception("Heap is empty")
        max_value = self.heap[0]
        self.heap[0] = self.heap[-1]  # Move last element to the root
        self.heap.pop()  # Remove last element
        self._heapify_down(0)  # Restore heap property
        return max_value

    def _heapify_up(self, i):
        # Ensures the heap property is maintained from the node upwards
        parent = (i - 1) // 2
        if i > 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._heapify_up(parent)

    def _heapify_down(self, i):
        # Ensures the heap property is maintained from the node downwards
        n = len(self.heap)
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify_down(largest)

    def __str__(self):
        return str(self.heap)

if __name__ == '__main__':

    # print(calculate_pie_values());
    heap = MaxHeap()
    heap.build_from_array([2,6,8,0,6])
    print(heap)
