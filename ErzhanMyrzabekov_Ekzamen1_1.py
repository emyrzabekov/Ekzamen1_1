# Задание 1:

#1
# x = int(str(float(5)))
# print(type(x))
# <class 'int'>

#2
# x = 'aa' == 'AA'
# print(type(x))
# <class 'bool'>

#3
# x = {i: i**2 for i in range(5)}
# print(type(x))
# <class 'dict'>

#4
# x = set(list((5, 6, 7)))
# print(type(x))
# <class 'set'>

#5
# a = {1: 1, 2: 4, 3: 9}
# x = a.get(4)
# print(type(x))
# <class 'bool(None)'>

#6
# x = [].append('j')
# print(type(x))
# <class 'bool(None)'>

#7
# for i in range(10):
#     if i < 5:
#         x = 'hello'
#     else:
#         x = 5
#     print(type(x))
# В данном случае тип данных Х будет пока значение i меньше 5: <class 'str'>, а дальше до 10 будет <class 'int'>.
# Если смотреть на Х за циклом то его типом данных будет <class 'int'>

#8
# x = input('Enter and integer: ')
# print(type(x))
# <class 'str'>

#9
# a = 5
# b = [1, 3, 5, ]
# x = 'x'
# a, b, x = x, a, b
# print(type(x))
# <class 'list'>

#10
# def func(x, y=5):
# 		return x + y
# x = func('Jaguar ', 'hunter')
# print(type(x))
# <class 'str'>
