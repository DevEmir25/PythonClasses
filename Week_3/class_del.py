class sinif:
    text = ""
    def __init__(self,a): #Constructor Method
        self.text = a

    def __del__ (self):
        print("asdas")

object = sinif("Text")

print(object.text)
del object