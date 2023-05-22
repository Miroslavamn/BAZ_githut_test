#ejemplo 1
my_dict = {"a":1, "b":2, "c":3}
try:
    value =my_dict["a"]
except KeyError:
    print("That key does not exist:")
else:
    print("Everithing is working perfect:")

#ejemplo 2
my_dict = {"a":1, "b":2, "c":3}
try:
    value =my_dict["Hola"]
except IndexError:
    print("That key does not exist:")
except KeyError:
    print("This key is not ")
else:
    print("Everithing is working perfect:")

