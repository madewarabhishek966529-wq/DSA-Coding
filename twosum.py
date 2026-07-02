ar = [10, 20, 30, 40, 50]

find = int(input("Enter sum: "))

found = False

for i in range(len(ar)):
    for j in range(i + 1, len(ar)):
        if ar[i] + ar[j] == find:
            print("Found:", ar[i], "+", ar[j], "=", find)
            found = True
            break
    if found:
        break

if not found:
    print("Not Found")