# 04_자료형

# 1. 수치형
# 1.1 int(정수)

print(10)        # 10
print(0b10)      # 2
print(0o10)      # 8
print(0x10)      # 16
print(type(10))  # <class 'int'>

# 1.2 float(실수, 부동소수점)

print(1.5)          # 1.5
print(-1.2)         # -1.2
print(type(3.313))  # <class 'float'>

print(4.2 - 4.1)    # 0.10000000000000053
print(5.6 - 5.5)    # 0.09999999999999964
# 부동소수점때문에 결과가 다르게 출력

a = 4.2 - 4.1
b = 5.6 - 5.5

# 해결_1 임의의 작은 수 활용
print(abs(a-b) <= 1e-10)  #True

# 해결_2 python 3.5 이상
import math
print(math.isclose(a, b))  #True

# 1.3 complex(복소수)

print(2+5j)          # (2+5j)
print(-5-2.5j)       # (-5-2.5j)
print(type(3-6.7j))  # <class 'complex'>

# 2. 문자열

print('hello')     # hello
print("hello")     # hello
print(type('hi'))  # <class 'str'>

print("Life is 'too' short!")  # Life is 'too' short!
print('Life is "too" short!')  # Life is "too" short!

print('''I would "love" to 
be good at 'Python'.''')

'''
I would "love" to
be good at 'Python'.
'''

print('1. Nice to \'see\' you')
print('2. Nice to see\n you')
print('3. Nice \t to see \\ you')
print('4. Nice \r4. Happy to see you')

'''
1. Nice to 'see' you
2. Nice to see
 you
3. Nice 	 to see \ you
4. Happy to see you
'''

# 2.1 문자열 연산

# 2.1.1 덧셈

print("Hello" + "World")  # HelloWorld

# 2.1.2 곱셉

print("Hello" * 3)  # HelloHelloHello

# 2.1.3 String Interpolation

# %-formatting

name = 'YM'
score = 3.81

print('Hello, %s' % name)       # Hello, YM
print('My score is %d' % score) # my score is 3.81
print('My score is %f' % score) # my score is 3.810000

# str.format()

print('Hello, {}! my score is {}'.format(name, score))
# Hello, YM! my score is 3.81

# f-strings : python 3.6+

print (f'Hello, {name}! my score is {score}')
# Hello, YM! my score is 3.81

import datetime
today = datetime.datetime.now()
print(today)    # 2022-08-17 22:12:04.333667

print(f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일')
# 오늘은 22년 07월 18일

pi = 3.141592
print(f'원주율은 {pi:.3}. 반지름이 4일 때 원의 넓이는 {pi*2*2}')
#원주율은 3.14. 반지름이 2일 때 원의 넓이는 12.566368

# 3. None

print(None) # None
print(type(None)) # <class 'NoneType'>

# 4. 불린형 (Boolean)

print(True)        # True
print(False)       # False
print(type(True))  # <class 'bool'>
print(type(False)) # <class 'bool'>
print(bool(-1))    # True
print(bool(0))     # False
print(2 > 3)       # False
print(type(3 < 5)) # <class 'bool'>

