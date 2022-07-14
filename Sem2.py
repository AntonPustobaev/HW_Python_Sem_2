# 1) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# def sum_num(a):
#     result = 0
#     for i in range(len(a)) :
#         if a[i]!= ',':
#             result += int(a[i])
#     print(f'{a} -> {result}')

# a = input('Введите число ')
# sum_num(a)



#2) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input('Введите N: '))

def GetChain(N):
    result = []
    for i in range(1, N+1):
        if i > 1:
            result.append(result[-1] * i)
        else:
            result.append(i)
    return result


print(f'N = {N}, тогда {GetChain(N)}')