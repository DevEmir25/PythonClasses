a = 5
while a < 10:
    a += 1
    if a == 8:
        continue
    if a == 12:
        break
    print(a)
else:
    print("a is now 15 or greater")