import modules_test

import modules_test as mod

print(modules_test.add(5,45))
print(modules_test.e)

print(mod.q)
class sinif:
    text = ""
    def __init__(self,a): #Constructor Method
        self.text = a

    def __del__ (self):
        print("asdas")

object = sinif("Text")

print(object.text)
del object