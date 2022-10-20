import random

secrets = {'Какая версия языка сейчас актуальна?': 'Python3',
        'Какая кодировка используется в строках?': 'UTF8',
        'Какой оператор сравнения нужно использовать'
        'для работы с None и bool?': 'is',
        'Сколько значений есть у bool?': '2',
        }

num_ques = 10
num_right_ans = 0

print('\nДавайте сыграем в игру загадки! Итак начнём!\n')

for index in range(num_ques):
    ki = random.choice(tuple(secrets.keys()))
    print('\tВопрос №{0}'.format(index + 1))
    print(ki)
    ans = input('Введите свой ответ: ')
    if secrets[ki].lower() == ans.lower():
        print('\nОтвет {0} верен'.format(ans))
        num_right_ans += 1
    else:
        print('\nНеверный ответ')

print('Игра закончилась!')
print('\tВаша статистика:')
print('Всего ответов - {0}'.format(num_ques))
print('Верных ответов - {0}'.format(num_right_ans))
print('Неверных ответов - {0}'.format(num_ques - num_right_ans))
