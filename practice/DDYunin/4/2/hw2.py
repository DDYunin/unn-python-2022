# class Array
class Array(object):

    # Конструктор (инициализирует данные)
    def __init__(self, *args):
        self.data = tuple(args)

    # Печатает элементы array
    def printdata(self):
        for index in self.data:
            print('Элемент массива = {0}'.format(index))
        print()

    # Добавляет элемент к array
    def append(self, arg):
        # Конструктор (инициализирует данные)
        self.data = self.data + (arg,)

    # складывает элементы array(складываем 2 tuple и распаковываем его с *)
    def __add__(self, array):
        return Array(*(self.data + array.data))

    # функция, которая выдаёт длину array
    def __len__(self):
        return len(self.data)

    # Определяет index элемента в array
    # Как будто есть ещё какой-то вариант
    def index(self, elem):
        if elem in self.data:
            return self.data.index(elem)
        return -1

    # позволяет получить значение array с помощью []
    def __getitem__(self, index):
        return self.data[index]

    # Позволяет делать итерацию в цикле for по array
    def __iter__(self):
        return iter(self.data)

# 1) Создавать себя как на примере: `Array()` - пустой списо,
#  `Array(1)` = список из одного объекта `1`, `Array(1, 2, 3)`


print('\nТест № 1\n')
array1 = Array()
array2 = Array(1)
array3 = Array(1, 'c', 'Hello', (2, 3, 4), 0.2)

# 2) Добавлять новый объект внутрь списка через метод `.append()`

print('\nТест № 2\n')
array2.printdata()
array2.append('Hello')
array2.printdata()

# 3) Складываться с другими `Array.Например:`Array(1) + Array(2) == Array(1, 2)`

print('\nТест № 3\n')
array4 = array2 + array3
array4.printdata()

# 4) Узнавать свою длину через функцию `len()`

print('\nТест № 4\n')
print('Длина Array d = {0}'.format(len(array4)))

# 5) находить индекс переданного объекта через метод `.index()`,возвращаем `-1`,
# если такого объекта в списке нет. Например: `Array('a', 'b').index('b') == 1`

print('\nТест № 5\n')
print(array4.index(1))
print(array4.index('c'))
print(array4.index(2))

# 6) Работать с циклом `for`: `for element in Array(1, 2, 3):`

print('\nТест № 6\n')
for elem in array4:
    print(elem)

# 7)Получать значение по индексу при помощи `[]`. Пример: `Array('a')[0] == 'a'`

print('\nТест № 7\n')
print(array4[0])
print(array4[3])
