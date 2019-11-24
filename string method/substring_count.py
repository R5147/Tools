def substring_count(old_string, search_string):
    if len(search_string) > len(old_string):
        return []
    result = []
    for i in range(len(old_string) - len(search_string) + 1):
        if old_string[i:i + len(search_string)] == search_string:
            if len(result) == 0:
                result.append(i)
            elif i > result[-1] + len(search_string) - 1:
                result.append(i)
    return result