'''
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
'''
#import cProfile

def lesson7(items):
    from random import randint as rand

    VARIANTS = [1, 100]
    #ITEMS = [5, 15]
    list_ = [rand(*VARIANTS) for _ in range(items)]

    min_index1 = len(list_)-1
    min_index2 = 0

    for i in range(len(list_)):
        if list_[i] <= list_[min_index1]:
            min_index1 = i
        else:
           min_index2 = i

    for i in range(len(list_)):
        if list_[i] < list_[min_index2] and i != min_index1:
            min_index2 = i

    return list_[min_index1], list_[min_index2]
    #print('В списке', list_)
    #print(f'два минимальных значения: {list_[min_index1]} и {list_[min_index2]}')




#cProfile.run('lesson7(100)')
#1    0.000    0.000    0.008    0.008 les3_task7.py:7(lesson7)
#cProfile.run('lesson7(1000)')
#1    0.000    0.000    0.009    0.009 les3_task7.py:7(lesson7)
#cProfile.run('lesson7(10000)')
#1    0.002    0.002    0.030    0.030 les3_task7.py:7(lesson7)
#cProfile.run('lesson7(100000)')
#1    0.018    0.018    0.223    0.223 les3_task7.py:7(lesson7)
#cProfile.run('lesson7(1000000)')
#1    0.175    0.175    2.167    2.167 les3_task7.py:7(lesson7)
#cProfile.run('lesson7(10000000)')
#1    1.654    1.654   21.070   21.070 les3_task7.py:7(lesson7)

#"les3_task7.lesson7(100)"
#100 loops, best of 5: 137 usec per loop
#"les3_task7.lesson7(1000)"
#100 loops, best of 5: 1.39 msec per loop
#"les3_task7.lesson7(10000)"
#100 loops, best of 5: 14 msec per loop

# Вывод: алгоритм имеет линейную сложность (O(n)),
# за исключением показаний cProfile.run('lesson7(____)') при значениях меньше '10000',
# вероятно ввиду слишком малых значений