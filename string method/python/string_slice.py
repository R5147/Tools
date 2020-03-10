def string_slice(string, start, end, step = 1):
    if end > len(string):
        return string
    if end <= start:
        return ''
    result = ''
    for i in range(start, end, step):
        result += string[i]
    return result

print(string_slice('abcdefg', 1, 3))
# bc
