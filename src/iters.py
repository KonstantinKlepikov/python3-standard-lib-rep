import more_itertools as mi

# библиотека возвращает итератор
# для некоторых функций доступен аргумент strict, если его 
# установит ьв True, то если длина последовательности не делится на n
# будет поднята ошибка ValueError

data = (1, 2, 3, 5, 6, 7, 44, 55, 66, 0, 'a')
data1 = [1, 2, 3, 5, 6, 7, 44, 55, 66, 0, 'a']

# chunked 
# сделать из последоватлеьности списки длиной n
# strict=False
res = mi.chunked(data, 2)
print(res)
print(list(res))


# ichunked
# возвращает генератор, возвращающий списки
res = mi.ichunked(data, 2)
print(res)

# sliced
# возвращает itertools.takewhile объект. Фактически это список объектов того же типа, что и исходный
# поддерживаются только последовательности, поддерживающие слайсинг
# strict=False
res = mi.sliced(data1, 3)
print(res)
print(list(res))

# distribute
# сделать n последовательностей по возможности равно длины. Это может порождать пустые списки
# возвращает список, состоязий из объектов itertools.slice
res = mi.distribute(6, data)
for i in res:
    print(list(i))

# divide
# список туплей-итераторов
res = mi.divide(3, data)
print(res)

# split_at
# разделить последовательность ровно по выбранному объекту (в итоговые последовательности объект не попадает)
# возвращается генератор списков
print(mi.split_at('abcdcba', lambda x: x == 'b'))
print(list(mi.split_at('abcdcba', lambda x: x == 'b')))
print(list(mi.split_at(range(10), lambda n: n % 2 == 1)))

# можно задать максимальное число сплитов
print(list(mi.split_at(range(10), lambda n: n % 2 == 1, maxsplit=2)))

# разделяющий элемент так-же можно сохранить в отдельной последовательности
print(list(mi.split_at('abcdcba', lambda x: x == 'b', keep_separator=True)))

# split_before()
# разделяет последовательность ровно перед позицией  разделителя

# split_after() понятно

# split_into()
# разделить на последовательности длин, равной переданной в списке длин
# получаем генератор, возвращающий списки
res = mi.split_into([1,2,3,4,5,6], [1,2,3])
print(res)
print(list(res))

# split_when()
# разделяет последовательность в том месте, где выполняется условие для предыдущего значения и последующего
# генератор возвращает списки
res = mi.split_when([1, 2, 3, 3, 2, 5, 2, 4, 2], lambda x, y: x > y)
print(res)
print(list(res))

# bucket
# создает bucket объект, который имеет АПИ слвоаря
# словарь заполянется так, чт оключ-  это условие, а значения - все подходящие объекты последовательности
# по ключу можно извлекать генераторы последовательностей этих объектов
iterable = ['a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'b3']
s = mi.bucket(iterable, key=lambda x: x[0])  # Bucket by 1st character
print(s)
print(list(s))
print(s['b'])
print(list(s['b']))

# unzip
# операция обрпатная zip
iterable = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
letters, numbers = mi.unzip(iterable)
print(list(letters))
print(list(numbers))

# grouper()
# создает zip_longest() объект зипуя последовательность в группы определенной длины, а нехватающую часть заполяняя филлером
res = mi.grouper('ABCDEFG', 3, 'x')
print(res)
print(list(res))

# partition()
# разделяет последовательность по условию так. что слева все что не удовлетворяет, а справа - удовлетворяет
is_odd = lambda x: x % 2 != 0
iterable = range(10)
even_items, odd_items = mi.partition(is_odd, iterable)
print(list(even_items), list(odd_items))

# spy
# возвращает список из первых n элементов и итератор всей последовательности
iterable = [1, 2, 3, 4, 5]
head, iterable = mi.spy(iterable, 3)
print(head)
print(list(iterable))

# peekable()
# создает итератор и список. Мы можем пикать следующий элемент сколько хотим раз или получать
# элементы последовательности по индексу. Некст передвигает "указатель"
# можно добавлять элементы в начало итератора
p = mi.peekable(['a', 'b'])
print(p.peek())
print(next(p))
print(p.peek(), p.peek())

p.prepend('12', '13')
print(p.peek())
print(next(p))
print(p.peek(), p.peek())
print(p[1])
print(list(p))

# seekable()
# можно ходить по итератору вперед и назад, указывая индекс эелемента
# peek() позволяет передвинуться вперед на один айтем без некста итератора
# кеш доступен через elements(), который возвращает уже израсходованные елементы
from itertools import count
it = mi.seekable((str(n) for n in count()))
print(it.elements())
print(next(it), next(it), next(it))
print(it.elements())
it.seek(0)
print(next(it), next(it), next(it))
('0', '1', '2')
print(next(it))
print('--------')
it.seek(0)
print(next(it))
print(it.peek())
print(next(it))
print(it.elements())
print(next(it))
print(it.elements())
it.seek(0)
print(it.elements())
