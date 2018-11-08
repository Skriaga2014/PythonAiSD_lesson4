'''
1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны любому из чисел в диапазоне от 2 до 9.
'''

#import cProfile

def lesson1(nums_do):

    NUMS_OT = 2
    #NUMS_DO = 1000000
    KRATN_OT = 2
    KRATN_DO = 9

    #print(f'В диапазоне от {NUMS_OT} до {NUMS_DO}:')

    kratn_dict = {}
    for i in range(KRATN_OT, KRATN_DO+1):
        n = 0
        for j in range(NUMS_OT, nums_do+1):
            if j % i == 0:
                n += 1
        kratn_dict[i] = n
        #print(f'количество чисел, кратных {i}: {n}')
    return kratn_dict

#cProfile.run('lesson1(10000)')
#1    0.006    0.006    0.006    0.006 les3_task1.py:8(lesson1)
#cProfile.run('lesson1(100000)')
#1    0.059    0.059    0.059    0.059 les3_task1.py:8(lesson1)
#cProfile.run('lesson1(1000000)')
#1    0.617    0.617    0.617    0.617 les3_task1.py:8(lesson1)

#"les3_task1.lesson1(10000)"
#100 loops, best of 5: 5.9 msec per loop
#"les3_task1.lesson1(100000)"
#100 loops, best of 5: 59.8 msec per loop
#"les3_task1.lesson1(1000000)"
#100 loops, best of 5: 593 msec per loop

# Вывод: алгоритм имеет линейную сложность (O(n))