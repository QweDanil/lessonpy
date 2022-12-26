a = []
b = int(input("Введите число: "))
while b != 0:
    a.append(b)
    b = int(input("Введите число : "))
a.sort(reverse=True)
print(a, sep="\r\n")
