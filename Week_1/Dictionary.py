dictionary = {
    "brand" : "audi",
    "model" : "A3",
    "year" : "2010"
}

print(dictionary)
print(dictionary["brand"])
print(dictionary["model"])
print(dictionary["year"])

dictionary["colour"] = "black"
print(dictionary)
print(dictionary["colour"])
dictionary["colour"] = "white"
print(dictionary)

print(dictionary.keys())
print(dictionary.values())

for i in dictionary.keys():
    print(i, ":", dictionary[i])