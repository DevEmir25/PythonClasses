class sinif:
    text = ""
    def __init__(self,a): #Constructor Method
        self.text = a

    def __str__ (self):
        return "Writed : " + self.text

object = sinif("Ziyaa")

print(object)
