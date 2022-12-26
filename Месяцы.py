a = str(input("Введите месяц: "))
match a.title():
    case("Январь"):
        print("31 день")
    case("Февраль"):
        print("28 или 29 дней")
    case("Март"):
        print("31 день")
    case("Апрель"):
        print("30 день")
    case("Май"):
        print("31 день")
    case("Июнь"):
        print("30 день")
    case("Июль"):
        print("31 день")
    case("Август"):
        print("31 день")
    case("Сентябрь"):
        print("30 день")
    case("Октябрь"):
        print("31 день")
    case("Ноябрь"):
        print("30 день")
    case("Декабрь"):
        print("31 день")
    case _:
        print("Такого месяца не существует")