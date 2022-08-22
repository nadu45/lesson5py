#                           lesson 5
#                            задание 1

my_f = open('test.txt', 'w')
line = input('Введите текст \n')
while line:
    my_f.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

my_f.close()
my_f = open('test.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()


#                            задание 2


with open("test.txt", "r", encoding='utf-8') as f_obj:
    useful = [f'{count}. {line.strip()} - {len(line.split())} слов'
              for count, line in enumerate(f_obj, 1)]
    print(*useful, f"Всего строк - {len(useful)}.", sep="\n")




my_file = open('test.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('test.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
my_file = open('test.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Окличество символов {i + 1} - ой строки {len(content[i])}')
my_file = open('test.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()


#                           задание 3

with open('test.txt', 'r') as my_file:
    sal = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')


#                           задание 4

my_f = open("test.txt", "r")
content = my_f.readline()
content = content[:-1]  # удаляем символ переноса строки
with open("test.txt", "w") as f_obj:
    print(content.replace('One', 'Один'), file=f_obj)

content = my_f.readline()
content = content[:-1]  # удаляем символ переноса строки
with open("test.txt", "a") as f_obj:
    print(content.replace('Two', 'Два'), file=f_obj)

content = my_f.readline()
content = content[:-1]  # удаляем символ переноса строки
with open("test.txt", "a") as f_obj:
    print(content.replace('Three', 'Три'), file=f_obj)

content = my_f.readline()
with open("test.txt", "a") as f_obj:
    print(content.replace('Four', 'Четыре'), file=f_obj)

#                          задание 5


def summary():
    try:
        with open('test.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()

#                            задание 6

import json

subj = {}
with open('test.txt', 'r') as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')


#                              задание 7


import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('test.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')

