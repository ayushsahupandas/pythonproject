file = open("sample.txt", "r")

print("First 5 characters:")
print(file.read(5))

file.seek(0)   # Move pointer to beginning
print("After seek(0):")
print(file.read(5))

file.close()
