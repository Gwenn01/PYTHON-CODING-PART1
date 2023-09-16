def string_reversal(s):
    #take the end length of string
    end = len(s) - 1
    result = ""
    # add it first so it will add as reverse
    for i in range(end, -1, -1):
        result += s[i]
    return result

print(string_reversal("hello world"))