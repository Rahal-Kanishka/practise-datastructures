# // COLLECTION OF NUMBERS
# FIND matching pair which equal to a sum
# [ 1,2, 3, 9] , sum = 8
# [1, 2,4 ,4], sum = 8

# ascending order
# integers, negatives and positives

def obvious(array, sum):
    # build two for loops and check for the target sum
    for index, i in enumerate(array):
        for j in range((index + 1), len(array)):
            if array[index] + array[j] == sum:
                return True
    return False

def usingHash(array, sum):
    dict = {}
    # insert items to hash table
    # for index, i in enumerate(array):
    #     dict[array[index]] = array[index]
    # then check the array and match with sum in the dict

    for i in array:
        if (sum-i) in dict:
            return True
        else:
            dict[i] = i
    print('dictionary: ', dict)
    return False



if __name__ == '__main__':
    print('response: ', usingHash([1, 2, 4, 5], 7))
