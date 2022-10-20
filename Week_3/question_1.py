# Kendisine gönderilen sayılardan sadece palindrom olanları toplayan diğerlerini de bu toplamdan çıkaran ve geri döndüren python fonksiyonunu
# yazınız.


my_list = []

numbers = int(input("how much number do you want: "))

for x in range(0,numbers):
    my_list.append(input('Enter a number: '))

def polindrom(dizi):
    total = 0
    for ispolindrom in dizi:
        if str(ispolindrom)[::-1] == str(ispolindrom):
            total += int(ispolindrom)
        else:
            total -= int(ispolindrom)
    print(total)

polindrom(my_list)









