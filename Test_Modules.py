import Febonachi as Feb
print("Вычисление ряда Фебоначи")
print("1 - найти ряд для заданного числа и вывести в консоль")
print("2 -  найти ряд для заданного числа и вывести в список")
user_choise = int(input("Ваш выбор:"))
if user_choise == 1:
    user_number = int(input("Найти ряд для числа:"))
    print(Feb.fib(user_number))
else:
    user_number = int(input("Найти ряд для числа:"))
    print(Feb.fib2(user_number))
