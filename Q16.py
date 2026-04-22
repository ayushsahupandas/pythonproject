def string_operations(s):
    print("Upper:", s.upper())
    print("Lower:", s.lower())
    print("Reversed:", s[::-1])

def list_operations(lst):
    lst.append(100)
    print("After append:", lst)
    print("Length:", len(lst))

string_operations("Python")
list_operations([1, 2, 3])
