def reverse(input_string):
    # o(n) solution
    result = ''
    i = len(input_string) - 1
    while i >= 0:
        result += input_string[i]
        i -= 1
    return result


if __name__ == '__main__':
    print(reverse('Hi Rahal'))
