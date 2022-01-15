def findMin(s):
    a, b = 0, 0
    while (s > 0):
        if (s % 7 == 0):
            b += 1
            s -= 7
        elif (s % 4 == 0):
            a += 1
            s -= 4
        else:
            a += 1
            s -= 4
    string = ""
    if (s < 0):
        string = "-1"
        return string
    string += "4" * a
    string += "7" * b
    return string
print(findMin(int(input())))
