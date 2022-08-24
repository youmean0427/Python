# 06_행 변환

# 6.1 암시적 형 변환

print(True + 3) #4
print(3 + 5.0) # 8.0

# 6.2 명시적 형 변환

# 6.2.1 int

print(int('3'))   # 3
print(int(3.5))   # 3
print(int(True))  # 1 
# print(int('3.5')) # ValueError

# 6.2.2 float

print(float('3'))   # 3.0
# print(float('3/4')) # ValueError
print(float(3))     # 3.0
print(float(3/4))   # 0.75

# 6.2.3 str

print(str(3))               # 3
print(type(str(3)))         # <class 'str'>
print(str(4.5))             # 4.5
print(str([1, 2, 3]))       # [1, 2, 3]
print(type(str([1, 2, 3]))) # <class 'str'>
print(str((1, 2, 3)))       # (1, 2, 3)
print(str({1 : 'one'}))     # {1: 'one'}

# 6.2.4 chr

print(chr(65))  # A
print(chr(48))  # 0

# 6.2.5 ord

print(ord('A')) # 65
print(ord('0')) # 48