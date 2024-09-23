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
        result.append(l1[len(l1) - 1 ])
    if l2[len(l2) - 1] not in result:
        result.append(l2[len(l2) - 1])
    return result


if __name__ == '__main__':
    print(merge_two_sorted_arrays([0, 3, 4, 31], [4, 6, 30]))
