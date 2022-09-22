# 09_함수

'''
def function_name(parameter):
	# Code
    return returning_value
'''

# ==========================
# 9.2 함수의 기본 구조
# ==========================

def function_1():
    return True

def add(x, y):
    return x + y

function_1()
add(2, 3)

num_1 = 3
num_2 = 5

def func_1(a, b):
    return a + b

def func_2(a, b):
    return a - b

def func_3(a, b):
    return func_1(a, 4) + func_2(4, b)

result = func_3(num_1, num_2)
print(result)

# ==========================
# 9.3 함수의 입력 (Input)
# ==========================

def function(x):
    return x
# parameter : x

function(y)
# argument : 'y'
# 함수 리턴 값 : y

# 9.3.1 Positional Arguments

def add(a, b):
    return a + b

add(1, 5)
# a = 1, b = 5

# 9.3.2 Keyword Arguments

def add(a, b):
    return a + b

add(1, 5)
add(1, y=5)
add(x=1, 5) # ERROR

# 9.3.3 Default Arguments Values

def add(a, b=0):
    return a + b

add(5)
# a = 5, y = 0

# ----------

print('CS')
# CS

print('CS', 'Study', 'Python')
# CS Study Python

# ----------

# 9.3.4 가변 인자 (*args)

def add(*args):
    for arg in args:
        print(arg)

add(4)
add(1, 2, 3, 4)


nums = (2, 4, 6, 8, 10) # 패킹
print(nums) # (2, 4, 6, 8, 10)

nums = (1, 2, 3, 4, 5) # 패킹
a, b, c, e, d = nums # 언패킹
print(a, b, c) #  1 2 3

a, b, c, e, d, f, g, h = nums # 언패킹, ValueError

a, b, c, *rest = nums # 1, 2, 3을 제외한 나머지 rest에 대입
print(a, b, c, rest) # 1, 2, 3, [4, 5]

a, *rest, e, d = nums # 1, 4, 5를 제외한 나머지 rest에 대입
print(rest) # [2, 3]


def func(*args):
	print(args)
	print(type(args))

func(0, 1, 'a', 'b')

'''
(0, 1, 'a', 'b')
<class 'tuple'>
'''


def sum_nums(*nums):
		result = 0
		for num in nums:
				result += num
		return result

print(sum_nums(0, 1, 2)) # 3
print(sum_nums(5, 6, 7, 8, 9)) # 35

def info(name, age, *emails):
	print(f'이름 : {name}')
	print(f'나이 : {age}')
	for email in emails:
		print(f'이메일 : {email}')

info('YM', '20', 'YM@gmail.com', 'YM@naver.com')

'''
이름 : YM
나이 : 20
이메일 : YM@gmail.com
이메일 : YM@naver.com
'''

# 9.3.5 가변 키워드 인자 (**kwargs)

def info (**kwargs):
		for key, value in kwargs.items():
			print(key,  ":", value)
info(name= 'YM', age= '20', email= 'YM@gmail.com')

'''
name : YM
age : 20
email : YM@gmail.com
'''


def info(name, age, **emails):
	print("이름 :", name)
	print("나이 :", age)
	if emails:
		for email_1, email_2 in emails.items():
			print(f'{email_1} : {email_2}')

info(name= 'YM', age= '20', email= 'YM@gmail.com', email= 'YM@naver.com')

'''
이름 : YM
나이 : 20
이메일 : YM@gmail.com
이메일 : YM@naver.com
'''


def info(*info, **emails):
	print("name :", info[0])
	print("age :", info[1])
	if pets:
		for title, name in emails.items():
			print('{} : {}'.format(title, name))

info(name= 'YM', age= '20', email= 'YM@gmail.com', email= 'YM@naver.com')

'''
이름 : YM
나이 : 20
이메일 : YM@gmail.com
이메일 : YM@naver.com
'''

# ==========================
# 9.4 함수의 결과값 (Output)
# ==========================

# Void function
print('Hello') # Hello

# Value returning function
float('1.23') # 1.23

# print는 값을 출력, 값을 반환하지는 않음


# Void function
def void_function(x, y):
    print(f'{x} + {y} = {x + y}')


void_function(4, 5)  # 4 + 5 = 9
ans = void_function(4, 5)
print(ans)  # None


# Value returning function
def value_returning_function(x, y):
    return x + y


value_returning_function(4, 5)
ans = value_returning_function(4, 5)
print(ans)  # 9


def plus_and_minus(x, y):
    return x + y
	return x - y

ans = plus_and_minus(9, 3)
print(ans) # 12

# 여러 개의 반환 → Tuple 활용 (or List)
def plus_and_minus(x, y):
    return x + y, x - y

ans = plus_and_minus(9, 3)
print(ans) # (12, 6)
print(type(ans)) # <class 'tuple'>