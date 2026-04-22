file = open("sample.txt", "r")

print("Using read():")
print(file.read())

file.seek(0)
print("Using readline():")
print(file.readline())

file.seek(0)
print("Using readlines():")
print(file.readlines())

file.close()
