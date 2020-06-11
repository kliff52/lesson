# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

# c = float
# def my_funk (a,b):
#     c = 0
#     try:
#         a = int(input('Vvedite pervoe znachenie - '))
#         b = int(input('Vvedite vtoroe znacghenie - '))
#         c = a / b or b / a
#     except ZeroDivisionError:
#         print('Deleniye na nol')
#         return
#     return c
# print(c)
# print(my_funk(None,None))


# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

# def my_func (name,surname,date,city,email,telephone):
#     return ' '.join([name, surname, date, city, email, telephone])
# print(my_func(surname = 'Анонимов', name = 'Аноним', date = '2001', city = 'Кунашак', email = 'g@g.g',
#               telephone = '8 800 2000 600'))

#
# def personal_func(**kwargs):
#     return kwargs
# print(personal_func(
#     name = input('Имя'),
#     surname = input("Фамилия"),
#     birthday = input('Дата рождения'),
#     city = input('Город'),
#     email = input('email'),
#     phone = input('Телефон'),
#     )
# )

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

# a = int(input('Vvedite pervoe znachenie'))
# b = int(input('Vvedite vtoroe znachenie'))
# c = int(input('Vvedite tretee znachenie'))
# def my_func2 (a,b,c):
#     if a >= c and b >= c:
#         return a + b
#     elif a > b and c > b:
#         return a + c
#     else:
#         return b + c
# print(my_func2(a,b,c))

#Преподовательский вариант решения.

# def my_func(num1,num2,num3):
#     try:
#         my_list = [num1,num2,num3]
#         my_list.pop(my_list.index(min(my_list)))
#         return sum(my_list)
#     except TypeError:
#         return 'Check number'
# print(my_func(1,2,3))

# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

# x = int(input('Vvedite polozhitelnoe chislo'))
# y = int(input('Vvedite celoe otricatelnoe chislo'))
# z = int
# def my_func(x,y):
#     z = x ** y
#     return z
# def my_func2(x,y):
#     z = 1 / (x ** -(y))
#     return z
# def fast_pow(x, y):
#     if y == 0:
#         return 1
#     if y == -1:
#         return 1. / x
#     p = fast_pow(x, y // 2)  #
#     p *= p
#     if y % 2:
#         p *= x
#     return p
#
#
# print(my_func(x,y))
# print(my_func2(x,y))
# print(fast_pow(x,y))

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее
# сумме и после этого завершить программу.
# def my_func_sum():
#     perm = False
#     result = 0 #переменная для суммы с суммой новыч чисел
#     while perm == False:
#         date = input('Vvedite chisla ili "E" dlya vihoda').split() #записываем и разделяем
#         res = 0    # Переменная для суммы внутреняя
#         for e1 in range(len(date)): #Идем по индексам
#             if date[e1] == 'e' or date[e1] == 'E':  # Выход по клавише Е или е
#                 print('Vvedena klasiha vihoda')
#                 perm = True     #для выхода из цикла
#                 break #скидываем
#             else:   # Если не введена клавиша
#                 print(res)
#                 res = res + int(date[e1]) #сложить предведущий результат с новым индексом
#         result = res + result #прибавить все к тому что было введенно
#         print('Summa novih chisel- ',res)
#         print('Summa vseh chisel- ',result)
# my_func_sum()

# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


# def int_func(text):
#     return text.title()
# print(int_func('text'))
# res_int_func = int_func('text bla text')
# print(res_int_func)