# Задание ​Формат: На семинаре и в лекциях мы разобрали новые функции, которые позволяют улучшить код прошлых задач.
# ​​Задача: предложить улучшения кода для уже решённых задач(не менее 4 задач нужно улучшить)

#Задача 2. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# num = int(input('Введите число: '))
# sum = 0
# for i in range(1, num+1):
#     sum += (1+1/i)**i
# print(round(sum, 2))

# Улучшение

# num = int(input('Введите число: '))
# lst = [(1+1/i)**i for i in range(1,num+1)]
# print(f"Полученная сумма последовательности (1+1/n)^n равнна {round(sum(lst),2)}")

#Задача 3. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# def multipl (num):
#     if num <=1:
#         return 1
#     else:
#         return (num * multipl(num-1))
# number = int(input('Введите число: '))
# for i in range(1, number):
#     print(multipl(i), end=', ')
# print(multipl(number))

# Улучшение

# from itertools import accumulate
# import operator

# number = int(input('Введите число: '))

# def multipl(number):
#     return list(accumulate([x for x in range(1, number + 1)], operator.mul))

# print(multipl(number))


#Задача 4. Сформировать список из  N членов последовательности.
#Для N = 5: 1, -3, 9, -27, 81 и т.д.

# number = int(input("Введите число: "))
# lst = []
# for i in range(number):
#     lst.append((-3)**i)
# print(f"Итоговая последовательность: {lst}")

# улучшение

# number = int(input("Введите число: "))
# lst = [(-3)**i for i in range(number)]
# print(f"Итоговая последовательность после применения list comprehension: {lst}")


#Задача 5. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# n = str(input('Введите число: '))
# sum = 0
# for i in n:
#     if i != '.' and i != ',':
#         sum += int(i)
# print(f'Сумма цифр в числе = {sum}')


# улучшение

# n = str(input('Введите число: '))
# new_sum = sum(map(int, str(n).replace('.', '')))
# print(f"Сумма цифр в числе = {new_sum}")



# Задача 6. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# # Пример:
# # - [2, 3, 4, 5, 6] => [12, 15, 16];
# # - [2, 3, 5, 6] => [12, 15]

# # list = [int(input(f'Введите {i+1} элемент списка: ')) for i in range(int(input('Введите количество элементов: ')))]
# # print(list) 

# # result_list = []
# # for i in range((len(list)+1)//2):
# #     result_list.append(list[i]*list[len(list)-1-i])
# # print(result_list)

# улучшение

def mult_lst(lst):
    l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    print(new_lst)

lst = list(map(int, input("Введите числа через пробел:\n").split()))
mult_lst(lst)

