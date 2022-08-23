# 05_컨테이너

# 5.1 리스트 (List)

list_1 = []
list_2 = [1, 2, 3]
list_3 = ['Hi', 'Hello', 'Bye']
list_4 = ['Hi', 3, ['Hello', 2]]

list_5 = list()
print(type(list_1)) # <class 'list'>
print(type(list_5)) # <class 'list'>

list_6 = ['I', 'My', 'Me', 'Mine']
print(list_6)       # ['I', 'My', 'Me', 'Mine']
print(type(list_6)) # <class 'list'>
print(list_6[0])    # I
print(list_6[2])    # Me

list_6[0] = 'You'
print(list_6) # ['You', 'My', 'Me', 'Mine']

# 5.2 튜플 (Tuple)

tuple_1 = (1, 2, 3, 4)
print(tuple_1)          # (1, 2, 3, 4)
print(type(tuple_1))    # <class 'tuple'>

print(tuple_1[3])      # 4
# tuple_1[2] = 2         # TypeError

tuple_2 = (1, )
print(tuple_2) # (1, )
print(type(tuple_2))  # <class 'tuple'>

tuple_3 = (1, 2, 3, )
print(tuple_3) # (1, 2, 3)
print(type(tuple_3))  # <class 'tuple'>

tuple_4 = 1,
tuple_5 = 1, 2, 3
print(tuple_4)       # (1, )
print(tuple_5)       # (1, 2, 3)
print(type(tuple_4)) # <class 'tuple'>
print(type(tuple_5)) # <class 'tuple'>

a, b = 4, 5
print(a, b) # 4 5

# 5.3 레인지 (Range)

# 5.3.1 기본형
print(list(range(4)))       # [0, 1, 2, 3]

# 5.3.2 범위 지정
print(list(range(2, 5)))    # [2, 3, 4]

# 5.3.3 범위 및 스텝 지정
print(list(range(3, 9, 2))) # [3, 5, 7]

# 역순
print(list(range(8, 1, -1))) # [8, 7, 6, 5, 4, 3, 2]
print(list(range(7, 2, -2))) # [7, 5, 3]
print(list(range(6, 0, 1)))  # []

# 5.4 슬라이싱 연산자

# 리스트
print([2, 4, 6, 7, 7][2:4]) # [6, 7]
# 튜플
print((1, 2, 3, 4)[1:3])    # (2, 3)
# 레인지
print(range(10)[5:9])       # range(5, 9)
# 문자열
print('abcdefg'[2:5])       # cde

# 시퀀스를 k 간격으로 슬라이싱

# 리스트
print([2, 4, 6, 7, 7][0:4:2])       # [2, 6]
# 튜플
print((1, 2, 3, 4, 5, 6, 7)[0:4:3]) # (1, 4)
# 레인지
print(range(10)[5:9:2])             # range(5, 9, 2)
# 문자열
print('abcdefg'[0:5:2])             # ace

n = 'kymcoding'

print(n[1:4])       # ymc
print(n[1:8:2])     # ycdn
print(n[8:2:-1])    # gnidoc
print(n[:5])        # kymco
print(n[2:])        # mcoding
print(n[::])        # kymcoding
print(n[::-1])      # gnidocmyk
print(n[-1:-8:-1])  # gnidocm

# 5.5 셋 (Set)

print({1, 2, 3, 4, 5, 1, 2, 3})  # {1, 2, 3, 4, 5}
print(type({1, 2, 3}))           # <class 'set'>

blank = {}
print(type(blank))       # <class 'dict'>
blank_set = set()
print(type(blank_set))   # <class 'set'>

# print({1, 2, 3}[0])    # Type Error

my_list = [11, 22, 33, 44]
print(my_list)           # [11, 22, 33, 44]
print(set(my_list))      # {33, 11, 44, 22}

Set_1 = {0, 1, 2, 3, 4}
Set_2 = {1, 2, 3, "Set", "SET", (1, 2, 3)}

print(Set_1 | Set_2)    # {0, 1, 2, 3, 4, 'SET', 'Set', (1, 2, 3)}
print(Set_1 & Set_2)    # {1, 2, 3}
print(Set_2 - Set_1)    # {'SET', 'Set', (1, 2, 3)}
print(Set_1 ^ Set_2)    # {0, 'SET', 4, 'Set', (1, 2, 3)}

# 5.6 딕셔너리 (Dictionary)

dict_1 = {}
dict_2 = {}

print(type(dict_1))  # <class 'dict'>

dict_1 = {'p' : 'python', 'j' : 'java', 'list' : [1, 2, 3]}
print(dict_1)       # {'p': 'python', 'j': 'java', 'list': [1, 2, 3]}
print(dict_1['j'])  # java

dict_2 = dict(p = 'python', j = 'java', list = [1, 2, 3])
print(dict_2)       # {'p': 'python', 'j': 'java', 'list': [1, 2, 3]}