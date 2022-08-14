# 03_연산자

# 1. 산술연산자

a = 9
b = 7

print(a + b)  # 16
print(a - b)  # 2
print(a * b)  # 63
print(a / b)  # 1.2857142857142858
print(a // b) # 1
print(a % b)  # 2
print(a ** b) # 4782969

# 2. 비교연산자

print(4 < 6)    # True
print(4 > 6)    # False
print(5 <= 3)   # False
print(5 >= 3)   # True
print(7 <= 7)   # True
print(8 >= 8)   # True

print(4.0 == 4) # sTrue
print('5' != 5) # True
print( 4 != 4)  # False
print(4 is 5)   # False
print(9 is 9)   # True

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)      # True
print(a is c)      # False
print(a is not b)  # False
print(b is not c)  # True

# 3. 논리연산자

print(1 and 1)  # 1
print(1 and 0)  # 0
print(0 and 1)  # 0
print(0 and 0)  # 0

print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False

print(1 or 1)  # 1
print(1 or 0)  # 1
print(0 or 1)  # 1
print(0 or 0)  # 0

print(True or True)   # True
print(True or False)  # True
print(False or True)  # True
print(False or False) # False

print(not True)  # False
print(not False) # True

# Falsy
print(bool(0))
print(bool(0.0))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(""))
print(bool(None))

print(True and not False or True) # True
print(False or True and False)    # False


print(4 and 6)  # 6
print(7 and 0)  # 0
print(0 and 9)  # 0
print(0 and 0)  # 0

print(9 or 5)  # 9
print(8 or 0)  # 8
print(0 or 2)  # 2
print(0 or 0)  # 0

a = 3 and 9
print(a)  # 9

b = 2 or 5
print(b)  # 2

c = 0 and 4
print(c)  # 0

d = 7 or 0
print(d)  # 7
