"""
задача: условий нет, что-то изменить в коде и направить ответ

!/usr/bin/env python
def x(a):
    return x(a - 1) + x(a - 2) + 42 if a > 1 else a
print ‘%r’ % x(195)
"""


def x(a):
    fib1 = 0
    fib2 = 1
    fib_sum = 0
    i = 0
    k = 0
    while i < a - 1:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i += 1
        k += fib1
    return 42*k + fib_sum


print('%r' % x(195))

# result: 1744559950484785950724677014047127864991062
