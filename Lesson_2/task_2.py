"""
Задача 6 *. Кинотеатр
X мальчиков и Y девочек пошли в кинотеатр и купили билеты на идущие подряд
места в одном ряду. Напишите программу, которая выдаст, как нужно сесть
мальчикам и девочкам, чтобы рядом с каждым мальчиком сидела хотя бы одна
девочка, а рядом с каждой девочкой — хотя бы один мальчик.
На вход подаются два числа: количество мальчиков X и количество девочек Y.
В ответе выведите какую-нибудь строку, в которой будет ровно X символов B,
обозначающих мальчиков, и Y символов G, обозначающих девочек,
удовлетворяющую условию задачи. Пробелы между символами выводить не
нужно. Если рассадить мальчиков и девочек согласно условию задачи
невозможно, выведите строку «Нет решения».


boys = int(input('Введите количество мальчиков: '))
girls = int(input('Введите количество девочек: '))

answer = ''

if (boys > 2 * girls) or (girls > 2 * boys):
    print('Нет решения')
elif boys >= girls:
    k = boys - girls
    for bgb in range(k):
        answer += 'BGB'
    for bg in range(girls - k):
        answer += 'BG'
else:
    k = girls - boys
    for gbg in range(k):
        answer += 'GBG'
    for gb in range(boys - k):
        answer += 'GB'

print(answer)


total_cards = int(input('Введите число карточек: '))

total_sum = 0

for card in range(1, total_cards + 1):
    total_sum += card

for card in range(total_cards - 1):
    remaining_card = int(input('Номер оставшейся карты: '))
    total_sum -= remaining_card

print('Номер потерявшейся карты', total_sum)


salary_year = 0

for month in range(1, 13):
    salary_month = int(input('Введите зарплату сотрудника за месяц {}: '.format(month)))
    salary_year += salary_month
average_salary = salary_year / 12

print('Средняя зарплата за год:', average_salary)


number = 7
guess_count = 0


while True:
    guess_num = int(input('Введите число: '))
    guess_count += 1
    if guess_num > number:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
    elif guess_num < number:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
    else:
        print('Вы угадали! Число потыток:', guess_count)
        break


hous = 0
tasks_sum = 0
go_to_store = False

print('Начался 8-часовой рабочий день')

while hous != 8:
    hous += 1
    print(hous, 'Час')
    solved_tasks = int(input('Сколько задач решит Максим? '))
    tasks_sum += solved_tasks
    call = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет): '))
    if call == 1:
        go_to_store = True

print('Рабочий день закончился. Всего выполнено задач:', tasks_sum)
if go_to_store:
    print('Нужно зайти в магазин')
"""

rating = int(input('Введите число: '))

positive_count = 0
negative_count = 0

while rating != 0:
    if rating > 0:
        positive_count += 1
    else:
        negative_count += 1
    rating = int(input('Введите число: '))

print('Кол-во положительных чисел:', positive_count)
print('Кол-во отрицательных чисел:', negative_count)


