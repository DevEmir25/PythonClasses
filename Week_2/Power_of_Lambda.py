"""
BUNUN KULLANILABİLECEĞİ BİR SINAV SORUSU SOR

"""
def my_function(n):
  return lambda a: a * n

get_fold = my_function(3)
print(get_fold(10))

get_fold = my_function(4)
print(get_fold(10))