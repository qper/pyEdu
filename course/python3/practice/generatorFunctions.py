def count_up_to(x):
    count = 1
    while count < x:
        yield count
        count += 1

counter = count_up_to(10)


for item in counter:
    print(item)



task = '''
Создайте функцию-генератор get_week_day(), которая создаёт генератор,
вырабатывающий один день недели за раз, Дни недели должны начинаться с воскресенья
и заканчиваться субботой.

current_day = get_week_day()
print(current_day.__next__()) # 'Sunday'
print(current_day.__next__()) # 'Monday'
print(current_day.__next__()) # 'Tuesday'
print(current_day.__next__()) # 'Wednesday'
print(current_day.__next__()) # 'Thursday'
print(current_day.__next__()) # 'Friday'
print(current_day.__next__()) # 'Saturday'
'''


def get_week_day():
    week_day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday']
    for item in week_day:
        yield item


current_day = get_week_day()
print(current_day.__next__()) # 'Sunday'
print(current_day.__next__()) # 'Monday'
print(current_day.__next__()) # 'Tuesday'
print(current_day.__next__()) # 'Wednesday'
print(current_day.__next__()) # 'Thursday'
print(current_day.__next__()) # 'Friday'
print(current_day.__next__()) # 'Saturday'



task2 = '''
Создайте функцию even_odd(), создающую генератор, который будет попеременно
вырабатывать строки 'even' и 'odd'.
even_odd_generator = even_odd()
print(next(even_odd_generator)) # 'even'
print(next(even_odd_generator)) # 'odd'
print(next(even_odd_generator)) # 'even'
print(next(even_odd_generator)) # 'odd'
'''

def even_odd():
    count = 0
    while True:
        if count %2 == 0:
            count += 1
            yield 'even'
        else:
            count += 1
            yield 'odd'

even_odd_generator = even_odd()
print(next(even_odd_generator)) # 'even'
print(next(even_odd_generator)) # 'odd'
print(next(even_odd_generator)) # 'even'
print(next(even_odd_generator)) # 'odd'

import time
from tqdm import tqdm

list_start_time = time.time()
list_from_generator = sum([i for i in tqdm(range(10**8))])
list_calculation_time = time.time() - list_start_time

print(list_from_generator)
print(list_calculation_time)


gen_start_time = time.time()
gen_from_generator = sum((i for i in tqdm(range(10**9))))
gen_calculation_time = time.time() - gen_start_time

print(gen_from_generator)
print(gen_calculation_time)



task3 = """
Создайте функцию, возвращающую генератор,
бесконечно вырабатывающий квадраты целых чисел, начиная с 1.
infinite_square_generator = get_infinite_square_generator()
print(next(infinite_square_generator)) # 1
print(next(infinite_square_generator)) # 4
print(next(infinite_square_generator)) # 9
print(next(infinite_square_generator)) # 16
...

"""

def get_infinite_square_generator():
    x = 1
    while True:
        yield x**2
        x += 1


infinite_square_generator = get_infinite_square_generator()

print(next(infinite_square_generator)) # 1
print(next(infinite_square_generator)) # 4
print(next(infinite_square_generator)) # 9
print(next(infinite_square_generator)) # 16
print(next(infinite_square_generator)) # 25
print(next(infinite_square_generator)) # 36
print(next(infinite_square_generator)) # 49
print(next(infinite_square_generator)) # 64
print(next(infinite_square_generator)) # 81
print(next(infinite_square_generator)) # 100
print(next(infinite_square_generator)) # 121
