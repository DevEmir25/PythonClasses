def add(*addition, extra = 0):
    total = 0
    for value in addition:
        total += value + extra
    return total

print(add(3, 5, 9, 15.2, 36, extra = 2), file="a.txt")