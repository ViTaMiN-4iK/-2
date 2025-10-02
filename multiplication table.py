def print_multiplication_table(size):
    for i in range(1, size):
        print()
        for j in range(1, size):
            print(f"{i} * {j} = {i * j}")


def print_multiplication_for_number(number):
    for i in range(1, 11):
        print(f"{i} * {number} = {i * number}")


def main():
    """Основная функция программы."""
    print("Выберите вариант работы:")
    print("1 - Полная таблица умножения")
    print("2 - Таблица умножения для конкретного числа")
    
    user_input = int(input("Выбор: "))
    
    if user_input == 1:
        print_multiplication_table(11)
    else:
        user_input_number = int(input("Таблица умножения для числа: "))
        print_multiplication_for_number(user_input_number)


if __name__ == "__main__":
    main()