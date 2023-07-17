# B. Определить вид последовательности
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# По последовательности чисел во входных данных определите ее вид:

# CONSTANT – последовательность состоит из одинаковых значений
# ASCENDING – последовательность является строго возрастающей
# WEAKLY ASCENDING – последовательность является нестрого возрастающей
# DESCENDING – последовательность является строго убывающей
# WEAKLY DESCENDING – последовательность является нестрого убывающей
# RANDOM – последовательность не принадлежит ни к одному из вышеупомянутых типов
# Формат ввода
# По одному на строке поступают числа последовательности ai, |ai| ≤ 109.

# Признаком окончания последовательности является число -2× 109. Оно в последовательность не входит.

# Формат вывода
# В единственной строке выведите тип последовательности.

# 5 < 4
def mon():
    x1 = int(input())
    if x1 == -2000000000:
        return 'RANDOM'
    x2 = int(input())
    CONSTANT = True
    ASCENDING = True
    WEAKLY_ASCENDING = True
    DESCENDING = True
    WEAKLY_DESCENDING = True
    while x2 != -2000000000:
        if x1 == x2:
            # print(x1, '=', x2)
            ASCENDING = False
            DESCENDING = False
        elif x1 > x2:
            # print(x1, '>', x2)
            CONSTANT = False
            ASCENDING = False
            WEAKLY_ASCENDING = False
        else:
            # print(x1, '<', x2)
            CONSTANT = False
            DESCENDING = False
            WEAKLY_DESCENDING = False
            
        x1 = x2
        x2 = int(input())

    if CONSTANT:
        return 'CONSTANT'
    elif ASCENDING:
        return 'ASCENDING'
    elif WEAKLY_ASCENDING:
        return 'WEAKLY ASCENDING'
    elif DESCENDING:
        return 'DESCENDING'
    elif WEAKLY_DESCENDING:
        return 'WEAKLY DESCENDING'
    else:
        return 'RANDOM'


print(mon())