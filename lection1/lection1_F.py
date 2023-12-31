"""
F. Расстановка ноутбуков
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
В школе решили на один прямоугольный стол поставить два прямоугольных ноутбука. 
Ноутбуки нужно поставить так, чтобы их стороны были параллельны сторонам стола. 
Определите, какие размеры должен иметь стол, чтобы оба ноутбука на него поместились, 
и площадь стола была минимальна.

Формат ввода
Вводится четыре натуральных числа, первые два задают размеры одного ноутбука, а 
следующие два — размеры второго. Числа не превышают 1000.

Формат вывода
Выведите два числа — размеры стола. Если возможно несколько ответов, выведите любой из них (но только один).

"""

def laptops(a1, b1, a2, b2):
    combinations = [
        (a1 + a2, max(b1, b2)),
        (a1 + b2, max(b1, a2)),
        (max(a1, a2), b1 + b2),
        (max(a1, b2), b1 + a2)
    ]

    return min(combinations, key=lambda y: y[0] * y[1])

a1, b1, a2, b2 = list(map(int, input().split()))
print(*laptops(a1, b1, a2, b2))