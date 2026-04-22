try:
    lst = [1, 2, 3]
    print(lst[5])
    num = int("abc")
except IndexError:
    print("Index out of range.")
except ValueError:
    print("Invalid conversion.")
