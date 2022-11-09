# 1) Профилировщик
# 2) Ручками, используя либу

# Что мы сегодня делали - измеряли, сколько памяти затрачивается при определённой строке в программе
# Смотрели на ассемблированный код
# Замеряли время работы, среднее, фрагмента кода

import dis
import timeit
from sys import getsizeof
from practice_7.task_2 import test1, test2

def check_memory_1():
    lst = list(range(1,10))
    print(lst)
    print(getsizeof(lst))
    tpl = tuple(range(1,10))
    print(tpl)
    print(getsizeof(tpl))

def check_memory_2():
    lst = list(range(1,10))
    print('Размер пустого списка = {0}'.format(getsizeof([])))
    lst2 = lst + lst
    print('Размер списка = {0}'.format(getsizeof(lst2)))
    tpl = tuple(range(1,10))
    tpl2 = tpl + tpl
    print('Размер кортежа = {0}'.format(getsizeof(tpl2)))
    print('Размер пустого кортежа = {0}'.format(getsizeof(())))

def check_memory_3():
    st = set(range(1,10))
    print('Размер множества = {0}'.format(getsizeof(st)))
    frst = frozenset(range(1,10))
    print('Размер множества = {0}'.format(getsizeof(frst)))

def check_memory_4():
    class PointA:
        x: int
        y: int
    class PointB:
        __slots__ = ['x', 'y']
        x: int
        y: int
    print(getsizeof(PointA))
    print(getsizeof(PointB))


def test3():
    lst1 = list(range(1,10))
    lst2 = lst1 + lst1
    print(lst2)


def test4():
    tpl1 = tuple(range(1,10))
    tpl2 = tuple(range(10,20))
    tpl3 = tpl1 + tpl2
    print(tpl3)

def test1(input_str: str):
    splits = []
    for char in (' ', ',', ';', ':', '.', '-', '_'):
         splits.append(input_str.split(char))
    return splits

def test2(input_str: str):
    splits = []
    append = splits.append
    split = input_str.split
    for char in (' ', ',', ';', ':', '.', '-', '_'):
         append(split(char))
    return splits

if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test4()
    # check_memory_4()
    dis.dis(test1)
    print('===========')
    dis.dis(test2)
    print('===========')
    print(timeit.timeit("test1('Привет, я Даня.')", setup='from __main__ import test1')/10000)
    print(timeit.timeit("test2('Привет, я Даня.')", setup='from __main__ import test2')/10000)
    