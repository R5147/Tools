def tc_number(n):
    # handle number from 0 - 999999999999
    if n > 999999999999:
        return -1
    words = [['零', '一', '二', '三', '四', '五', '六', '七', '八', '九'], '十', '百', '千', '萬', '十萬', '百萬', '千萬', '億']
    n_digit_length = len(str(n))
    number_list = []
    number_list_2 = []
    result = ''

    for i in range(n_digit_length):
        unit = 10 ** (n_digit_length - 1 - i)
        cur_num = int(str(n)[i]) * unit
        number_list.append(cur_num)

    for i in number_list:
        current_digit_length = len(str(i))
        unit = 10 ** (current_digit_length - 1)
        if current_digit_length > 9:
            current_digit_length = len(str(int(i/100000000)))
            unit = 10 ** (current_digit_length - 1)
            if current_digit_length > 1:
                number_list_2.append(int(int(i / 100000000) / unit))
                number_list_2.append(unit)
            else:
                number_list_2.append(int(i / 100000000))
            number_list_2.append(100000000)
        elif current_digit_length != 1:
            number_list_2.append(int(i/unit))
            number_list_2.append(unit)
        else:
            number_list_2.append(i)

    if n != 0:
        number_list = []
        for i in range(len(number_list_2)):
            if number_list_2[i] == 0 and number_list_2[i-1] != 0:
                number_list.append(0)
            elif number_list_2[i] != 0:
                number_list.append(number_list_2[i])
        if number_list[-1] == 0:
            number_list = number_list[:-1]
        number_list_2 = number_list

    for i in number_list_2:
        current_digit_length = len(str(i))
        if current_digit_length == 1:
            result += words[0][i]
        else:
            result += words[current_digit_length-1]

    if (n >= 10 and n < 20) or (n >= 100000 and n < 200000) or (n >= 1000000000 and n < 2000000000):
        result = result[1:]

    for i in range(1, result.count(words[4])):
        result = result.replace(words[4], '', 1)
    for i in range(1, result.count(words[8])):
        result = result.replace(words[8], '', 1)

    return result
