dosya = open("kod.txt" , 'w')
print("print('legendary python')" , file = dosya)
dosya.close()

dosya = open("kod.txt" , 'r')
line = dosya.readline()
exec(line)
