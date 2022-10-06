a = [1, 2, 3]
b = [False, 0.2, 8798765456, None, [2, "ho", 17.5]]

print(a)
print(b)
print(b[0])
print(b[4][1])

tr = "Türkiye"
print(tr[1:4]) #gets character from 1 to 4

b[2] = 5456134894
print(b)

def function(n):
    return abs(n - 50) #get absolute value of the number

number_list = [100, 50, 65, 82, 23]
number_list.sort(key = function)
print(number_list)