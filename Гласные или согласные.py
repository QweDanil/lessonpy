a = str(input("Введите букву латинского алфавита: "))

match a:
    case("a"):
        print("Гласная")
    case("e"):
        print("Гласная")
    case("i"):
        print("Гласная")
    case("u"):
        print("Гласная")
    case("y"):
        print("Гласная и согласная")
    case _:
        print("Согласная")