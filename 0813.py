def mostfrequentletter(string):
    string = string.lower
    frequent = string[0]
    for i in range(1, len(string)):
        if string.count(string[i])>string.count(frequent):
            frequent = string[i]
        elif string.count(string[i]) = string.count(frequent):
            if ord(string[i])<=ord(string[i]):
                frequent = string[i]
    return frequent