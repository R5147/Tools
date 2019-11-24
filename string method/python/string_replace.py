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


def string_replace(old_string, search_string, replace_string, replacement=-1):
    if len(search_string) > len(old_string):
        return old_string
    result_string = old_string
    replace_points = substring_count(old_string, search_string)

    if replacement < 0 or replacement >= len(replace_points):
        for i in range(len(replace_points)):
            result_string = result_string[:replace_points[i] + (len(replace_string) - len(search_string)) * i] + replace_string + result_string[replace_points[i] + (len(replace_string) - len(search_string)) * i + len(search_string):]
    elif replacement > 0:
        for i in range(replacement):
            result_string = result_string[:replace_points[i] + (len(replace_string) - len(search_string)) * i] + replace_string + result_string[replace_points[i] + (len(replace_string) - len(search_string)) * i + len(search_string):]

    return result_string


