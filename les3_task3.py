'''
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

import cProfile

def lesson3(items):
    from random import randint as rand

    VARIANTS = [-100, 100]
    #ITEMS = [20000, 20000]

    list_ = [rand(*VARIANTS) for _ in range(items)]
    max = list_[0]
    min = list_[0]

    for i in list_:
        if i > max:
            max = i
        if i < min:
            min = i

    #print(f'Оригинальный список: {list_}')
    #print(f'min = {min}')
    #print(f'max = {max}')
    #print(f'Меняем значения {min} и {max} местами:')
    list_[list_.index(min)], list_[list_.index(max)] = list_[list_.index(max)], list_[list_.index(min)]
    return list_

#cProfile.run('lesson3(10**2)')
#1    0.000    0.000    0.007    0.007 les3_task3.py:7(lesson3)
#cProfile.run('lesson3(10**3)')
#1    0.000    0.000    0.009    0.009 les3_task3.py:7(lesson3)
#cProfile.run('lesson3(10**4)')
#1    0.001    0.001    0.027    0.027 les3_task3.py:7(lesson3)
#cProfile.run('lesson3(10**5)')
#1    0.006    0.006    0.208    0.208 les3_task3.py:7(lesson3)
#cProfile.run('lesson3(10**6)')
#1    0.060    0.060    2.062    2.062 les3_task3.py:7(lesson3)
#cProfile.run('lesson3(10**7)')
#1    0.563    0.563   20.139   20.139 les3_task3.py:7(lesson3)

#"les3_task3.lesson3(10**2)"
#100 loops, best of 5: 136 usec per loop
#"les3_task3.lesson3(10**3)"
#100 loops, best of 5: 1.34 msec per loop
#"les3_task3.lesson3(10**4)"
#100 loops, best of 5: 13.3 msec per loop

# Вывод: алгоритм имеет линейную сложность (O(n)),
# за исключением показаний cProfile.run('lesson3(10**2)'),
# вероятно ввиду слишком малых значений