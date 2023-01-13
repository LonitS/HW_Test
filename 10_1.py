def rev_list(data):
    result = data.copy()
    for i in range(len(data))[2::2]:
        result[i - 1] = data[i - 1][::-1]
    return result


def a_filter(data):
    result = []
    for string in data:
        if string[0] == 'a':
            result.append(string)
    return result


def a_finder(data):
    result = []
    for string in data:
        if 'a' in string:
            result.append(string)
    return result


def only_str(data):
    result = []
    for string in data:
        if type(string) == str:
            result.append(string)
    return result


def uni(data):
    result = ''
    for i in set(data):
        count = sum(map(lambda x: 1 if i in x else 0, data))
        if count == 1:
            result += i
    return result


def func_6(string_1, string_2):
    temp = set(string_1 + string_2)
    result = []
    for i in temp:
        if i in string_1 and i in string_2:
            result.append(i)
    return result


def func_7(string_1, string_2):
    string_1 = uni(string_1)
    string_2 = uni(string_2)
    temp = set(string_1 + string_2)
    result = []
    for i in temp:
        if i in string_1 and i in string_2:
            result.append(i)
    return result


def main():
    my_list = ["aone", "atwo", "three", "four", "afive", "sixa"]
    d_list = [1, 2, 3, 4, 5, 6]
    my_string = 'oan^foaneoanlmovnaovndj@d1111'
    my_string_2 = '1234567!@#$%^'
    print(f'Input list 1: {my_list}')
    print(f'Input list 2: {d_list}')
    print(f'Input string 1: {my_string}')
    print(f'Input string 1: {my_string_2}')

    result_list = rev_list(my_list)
    print(f'Result 1 Func: {result_list}')
    result_list = a_filter(my_list)
    print(f'Result 2 Func: {result_list}')
    result_list = a_finder(my_list)
    print(f'Result 3 Func: {result_list}')
    my_list = my_list + d_list
    result_list = only_str(my_list)
    print(f'Result 4 Func: {result_list}')
    result_string = uni(my_string)
    print(f'Result 5 Func: {result_string}')
    result_string = func_6(my_string, my_string_2)
    print(f'Result 6 Func: {result_string}')
    result_string = func_7(my_string, my_string_2)
    print(f'Result 7 Func: {result_string}')


if __name__ == "__main__":
    main()
