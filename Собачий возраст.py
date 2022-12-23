a = int(input("Введите возраст собаки: "))

if(a <= 0):
   print("Ошибка")
elif(a == 1):
   print(10.5)
elif(a == 2):
   print(30)
else:
   print(30+((a-2)*4))
