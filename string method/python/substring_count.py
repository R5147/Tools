def substring_count(old_string, search_string):
    result = []
    if len(search_string) > len(old_string):
        return result
    for i in range(len(old_string) - len(search_string) + 1):
        if old_string[i:i + len(search_string)] == search_string:
            if len(result) == 0:
                result.append(i)
            elif i > result[-1] + len(search_string) - 1:
                result.append(i)
    return result



# example [start]
string = "Hello world!"
find = "l"
print(len(substring_count(string, find)))
# 3
print(substring_count(string, find))
# [2, 3, 9]

find = "ll"
print(len(substring_count(string, find)))
# 1
print(substring_count(string, find))
# [2]
# example [end]

