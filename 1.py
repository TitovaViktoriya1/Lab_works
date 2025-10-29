def main():
    print("Здравствуйте! 👋")
    print("Это универсальный конвертер единиц измерения.")
    
    while True:
        print("\nВыберите тип конвертации:")
        print("1. Метры → Километры")
        print("2. Километры → Метры")
        print("3. Градусы Цельсия → Фаренгейты")
        print("4. Фаренгейты → Градусы Цельсия")
        print("5. Килограммы → Фунты")
        print("6. Фунты → Килограммы")
        print("7. Метры в секунду → Километры в час")
        print("8. Километры в час → Метры в секунду")
        print("9. Сантиметры → Дециметры")
        print("10. Дециметры → Сантиметры")
        print("0. Выход")

        choice = input("\nВведите номер варианта: ")

        if choice == "0":
            print("До свидания! 👋")
            break

        try:
            value = float(input("Введите значение для конвертации: "))
        except ValueError:
            print("Ошибка: нужно ввести число.")
            continue

        if choice == "1":
            result = value / 1000
            print(f"{value} м = {result} км")
        elif choice == "2":
            result = value * 1000
            print(f"{value} км = {result} м")
        elif choice == "3":
            result = (value * 9/5) + 32
            print(f"{value} °C = {result} °F")
        elif choice == "4":
            result = (value - 32) * 5/9
            print(f"{value} °F = {result} °C")
        elif choice == "5":
            result = value * 2.20462
            print(f"{value} кг = {result} фунтов")
        elif choice == "6":
            result = value / 2.20462
            print(f"{value} фунтов = {result} кг")
        elif choice == "7":
            result = value * 3.6
            print(f"{value} м/с = {result} км/ч")
        elif choice == "8":
            result = value / 3.6
            print(f"{value} км/ч = {result} м/с")
        elif choice == "9":
            result = value / 10
            print(f"{value} см = {result} дм")
        elif choice == "10":
            result = value * 10
            print(f"{value} дм = {result} см")
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
