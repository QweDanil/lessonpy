a = []
b = str(input("Введите число: "))
while b != "rom":
    b = str(input("Введите число : "))
    if not b:
        break
    elif b not in a:
        a.append(b)
a.sort()
print(a, sep="\r\n")
