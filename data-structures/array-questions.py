def merge_two_sorted_arrays(l1, l2):
    # im going to find minimum and then move it to a new array and repeat.
    result = []
    i = 0
    j = 0
    max = l1[0]
    for item1 in l1:
        for item2 in l2:
            print(item1, item2, result)
            if item1 < item2:
                result.append(item1)
                # print('result: ', result)
                break
            else:
                if item2 not in result:
                    result.append(item2)
                # l2.remove(item2)
            # print('result: ', result)
    # check any last items from either of the array is not inserted
    if l1[len(l1) - 1] not in result:
        result.append(l1[len(l1) - 1])
    if l2[len(l2) - 1] not in result:
        result.append(l2[len(l2) - 1])
    return result


# used O(n) solution instead of the O(N^2)
def merge_two_sorted_arrays_better_solution(l1, l2):
    # handling empty scenarios
    if l1 is None or len(l1) == 0:
        return l2
    if l2 is None or len(l2) == 0:
        return l1

    item1 = l1[0]
    item2 = l2[0]
    result = []
    i = 1
    j = 1

    while item1 is not None or item2 is not None:
        print(len(result), result, item1, item2, ' i,j: ', i, j, )

        if item1 is None and item2:
            result.append(item2)
            if j < len(l2):
                item2 = l2[j]
                j += 1
            else:
                item2 = None
        elif item2 is None and item1:
            result.append(item1)
            if i < len(l1):
                item1 = l1[i]
                i += 1
            else:
                item1 = None
        elif item2 is None and item1 is None:
            break
        elif item1 and item2:
            if item1 < item2:
                result.append(item1)
                if i < len(l1):
                    item1 = l1[i]
                    i += 1
                else:
                    item1 = None
            else:
                result.append(item2)
                if j < len(l2):
                    item2 = l2[j]
                    j += 1
                else:
                    item2 = None

    print('loop ends', item1, item2, ', i,j: ', i, j, 'result: ', result)
    return result


if __name__ == '__main__':
    # print(merge_two_sorted_arrays([0, 3, 4, 31], [4, 6, 30]))
    print(merge_two_sorted_arrays_better_solution([10, 80], [33, 55, 66, 77, 79]))
