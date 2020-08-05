#1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('test.txt', 'w') as b:
    while True:
        text = input('Введите что угодно: ')
        if text == '':
            break
        b.write(text + '\n')


#2. Создать текстовый файл (не программно), сохранить в нем несколько
# строк, выполнить подсчет количества строк, количества слов в каждой строке.

with open('test_1.txt') as b:
    text = b.readlines()
    print('Кол-во строк: ', len(text))
    for line_number, line in enumerate(text, start=1):
        print('{} Cтрока содержит - {} слов'.format(line_number, len(line.split())))

#3.Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину
# их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих
# сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open('test_3') as b:
    salary_1 = []
    lines = b.readlines()
    for line in lines:
        name, salary = line.split('=')
        salary_1.append(int(salary))
        if int(salary) < 20000:
            print(line, end='')
    print('\nСредняя зп:', sum(salary_1) / len(salary_1))

#4. Создать (не программно) текстовый файл со следующим содержимым:

with open('eng.txt', encoding='utf-8') as b:
    line = b.readlines()

with open('rus.txt', 'w', encoding='utf-8') as b:
    for text in line:
        if '1' in text:
            text = text.replace('One', 'Один')
        elif '2' in text:
            text = text.replace('Two', 'Два')
        elif '2' in text:
            text = text.replace('Three', 'Три')
        elif '2' in text:
            text = text.replace('Four', 'Четыре')
        b.write(text)

#5. Создать (программно) текстовый файл, записать в него программно
# набор чисел, разделенных пробелами. Программа должна подсчитывать
# сумму чисел в файле и выводить ее на экран.

with open('5.txt', 'w') as b:
    number = input('Введите числа через пробел: ')
    b.write('Введите числа: ' + number + '\n')
    number = map(int, number.split())
    sum_number = sum(number)
    b.write('Сумма чисел: ' + str(sum_number))
    print('Сумма введенных чисел: ', sum_number)
print('Записано в файл')

#6. Необходимо создать (не программно) текстовый файл, где каждая строка
# описывает учебный предмет и наличие лекционных, практических и лабораторных
# занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий. Сформировать словарь, содержащий название
# предмета и общее количество занятий по нему. Вывести словарь на экран.

my_dict = dict()
with open('6.txt') as b:
    lines = b.readlines()
    for text in lines:
        sp_line = text.split()
        sp_line_2 = sp_line[0]
        sum_lesson = sum([int(x[:x.find('(')]) for x in sp_line[1:] if '(' in x])
        my_dict[sp_line_2] = sum_lesson
print(my_dict)