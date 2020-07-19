#1 Создать список и заполнить его элементами различных типов данных.
#Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type()
#для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

simple_kod = {200, 23.6, 'text', True }
for i in simple_kod:
    print(type(i))

#2 Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с
#индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
#Для заполнения списка элементов необходимо использовать функцию input()

my_work = list(input('Введите текст - '))
for i in range(1, len(my_work), 2):
    my_work[i - 1], my_work[i] = my_work[i], my_work[i-1]
print(my_work)

#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = int(input('Введите месяц: - '))
if month <= 0 or month >= 13:
    print('Введен неверный месяц')
elif month >= 3 and month <= 5:
    print('Весна')
elif month >= 6 and month <= 8:
    print('Лето')
elif month >= 9 and month <= 11:
    print('Осень')
else:
    print('Зима')

#2й вариант
seasons_dict = {
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
    4: 'Апрель',
    5: 'Май',
    6: 'Июнь',
    7: 'Июль',
    8: 'Август',
    9: 'Сентябрь',
    10: 'Октябрь',
    11: 'Ноябрь',
    12: 'Декабрь',
}
month = int(input('Введите месяц - '))
print(seasons_dict[month])

#4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

text = input()
words = text.split()
for i, word in enumerate (words):
    print(i, word[:10])

#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий
# набор натуральных чисел. У пользователя необходимо запрашивать новый элемент
# рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
usr_num = int(input())
if min(my_list) > usr_num:
    my_list.append(usr_num)
else:
    for i, num in enumerate(my_list):
        if usr_num >= num:
            my_list.insert(i, usr_num)
            break
print(my_list)