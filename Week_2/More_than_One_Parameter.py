

def add_all_values(*a):
    total = 0
    for value in a:
        total += value
    return total


print(add_all_values(4, 8, 15, 20.2, 40))