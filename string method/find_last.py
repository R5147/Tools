def string_len(string):
    n = 0
    for i in string:
        n += 1
    return n

def find_last(string, target):
    if string_len(target) > string_len(string):
        return -1
    n = string_len(string) - (string_len(target) - 1)
    last_pos = -1
    for i in range(n):
        if string[i:i + string_len(target)] == target:
            last_pos = i
    return last_pos
