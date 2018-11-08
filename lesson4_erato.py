'''
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Первый - использовать алгоритм решето Эратосфена.
Второй - без использования "решета".
Проанализировать скорость и сложность алгоритмов.
'''
#import cProfile

def eratosfen(limit):
    if limit == 0:
        return 0
    erato_list = [2]
    m = 2
    ind = 0
    while ind < limit-1:
        m += 1
        if m < 8 and m != 4 and m != 6 or m % 2 != 0 and m % 3 != 0 and m % 5 != 0 and m % 7 != 0:
            ind += 1
            erato_list.append(m)
        else:
            erato_list.append(0)
    return erato_list[-1]

#cProfile.run('eratosfen(1000)')
#1    0.002    0.002    0.002    0.002 lesson4-erato.py:9(eratosfen)
#cProfile.run('eratosfen(10000)')
#1    0.016    0.016    0.019    0.019 lesson4-erato.py:9(eratosfen)
#cProfile.run('eratosfen(100000)')
#1    0.154    0.154    0.185    0.185 lesson4-erato.py:9(eratosfen)

#"lesson4_erato.eratosfen(100)"
#100 loops, best of 5: 113 usec per loop
#"lesson4_erato.eratosfen(1000)"
#100 loops, best of 5: 1.31 msec per loop
#"lesson4_erato.eratosfen(10000)"
#100 loops, best of 5: 13.3 msec per loop


# Вывод: алгоритм имеет линейную сложность (O(n)),
# однако создает лишние данные (нули в списке), расходуя на это время.

def prost_num(n):
    m = 2
    ind = 0
    while ind < n-1:
        m += 1
        if m < 8 and m != 4 and m != 6 or m % 2 != 0 and m % 3 != 0 and m % 5 != 0 and m % 7 != 0:
            ind += 1
    return m

#cProfile.run('prost_num(1000)')
#1    0.001    0.001    0.001    0.001 lesson4-erato.py:32(prost_num)
#cProfile.run('prost_num(10000)')
#1    0.010    0.010    0.010    0.010 lesson4-erato.py:32(prost_num)
#cProfile.run('prost_num(100000)')
#1    0.103    0.103    0.103    0.103 lesson4-erato.py:32(prost_num)

#"lesson4_erato.prost_num(100)"
#100 loops, best of 5: 82.9 usec per loop
#"lesson4_erato.prost_num(1000)"
#100 loops, best of 5: 996 usec per loop
#"lesson4_erato.prost_num(10000)"
#100 loops, best of 5: 10.1 msec per loop

# Вывод: алгоритм имеет линейную сложность (O(n)),
# лишние данные не создает, ввиду чего время выполнения сократилось на:
# 44% по данным cProfile.run('________(100000)')
# 24% по данным timeit (100 loops)



#print(eratosfen(10000))
#print(prost_num(10000))

