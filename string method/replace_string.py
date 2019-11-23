def string_replace(old_string, search_string, replace_string, replacement=-1):
    if len(search_string) > len(old_string):
        return old_string
    result_string = old_string

    if replacement == -1:
        new_length = 0
        for i in range(len(old_string) - len(search_string) + 1):
            if old_string[i:i + len(search_string)] == search_string:
                if len(result_string) == len(old_string):
                    result_string = result_string[:i] + replace_string + result_string[i + len(search_string):]
                else:
                    new_length += len(replace_string) - len(search_string)
                    result_string = result_string[:i + new_length] + replace_string + result_string[i + new_length + len(search_string):]
    else:
        pass

    return result_string
