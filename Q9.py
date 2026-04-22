# Q9: break, continue, pass

print("Using break:")
for i in range(1, 6):
    if i == 4:
        break
    print(i)

print("\nUsing continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("\nUsing pass:")
for i in range(1, 6):
    if i == 3:
        pass
    print(i)
