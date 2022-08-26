# 08_제어문 (반복문)

# 반복문

# ---------------------
# while
# ---------------------

num = 0
while num < 10:
    print(num)
    num += 1
print('end')
'''
0
1
2
3
4
5
6
7
8
9
end
'''

# ---------------------
# for
# ---------------------

for number in ['one', 'two', 'three']:
    print(number)
print('next?')

'''
one
two
three
next?
'''

# 문자열 (String) 순회

chars = 'Attention'

for i in chars:
    print(i, end = " ")
    # A t t e n t i o n
print()
for idx in range(len(chars)):
    print(chars[idx])
'''
A
t
t
e
n
t
i
o
n
'''

# 딕셔너리 (Dictionary) 순회
# 기본적으로 key를 순회, key로 value를 활용

scores = {'Kim': 40, "Lee": 20}
for i in scores:
    print(i)

'''
Kim
Lee
'''

for j in scores:
    print(j, scores[j])

'''
Kim 40
Lee 20
'''

for n, m in scores.items():
    print(n, m)

'''
Kim 40
Lee 20
'''

print(scores.keys())
print(scores.values())
print(scores.items())

'''
dict_keys(['Kim', 'Lee'])
dict_values([40, 20])
dict_items([('Kim', 40), ('Lee', 20)])
'''

# Enumerate 순회
# Index와 Value를 쌍으로 담은 객체 반환
# (Index, Value) 튜플 반환

members = ['K', 'W', 'N', 'Z']

for idx, name in enumerate(members):
    print(idx, name)

'''
0 K
1 W
2 N
3 Z
'''

enumerate(members)
print(list(enumerate(members)))			 # [(0, 'K'), (1, 'W'), (2, 'N'), (3, 'Z')]
print(list(enumerate(members, start=1))) # [(1, 'K'), (2, 'W'), (3, 'N'), (4, 'Z')]

# List Comprehension

# 제곱 리스트 만들기
result_list = []
for number in range(1, 6):
    result_list.append(number ** 2)
print(result_list)
# [1, 4, 9, 16, 25]

result_list = [number ** 2 for number in range(1, 6)]
print(result_list)
# [1, 4, 9, 16, 25]

# Dictionary Comprehension

# 제곱 딕셔너리 만들기
result_dict = {}
for number in range(1, 6):
    result_dict[number] = number ** 2
print(result_dict)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

result_dict = {number: number ** 2 for number in range(1, 6)}
print(result_dict)
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# ---------------------
# 반복문 제어
# ---------------------

# break

num = -1
while True:
    if num == 2:
        break
    print(num)
    num += 1

'''
-1
0
1
'''

for i in range(20):
    if i > 10:
        print("10 이상")
        break
    print(i)
'''
0
1
2
3
4
5
6
7
8
9
10
10 이상
'''

# continue

for i in range(50):
    if i % 2 == 0:
        continue
    print(i, end= " ")
# 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49

# for-else

for name in 'YMYM':
    if name == 'K':
        print('Kim')
        break
else:
    print('No, Kim')
# No, Kim

for name in 'YMYM':
    if name == 'M':
        print('Min')
        break
else:
    print('No, Kim')
# # Min

# Pass

for i in range(10):
    if i == 4:
        pass
    print(i, end= ' ')
# 0 1 2 3 4 5 6 7 8 9

for i in range(10):
    if i == 4:
        continue
    print(i, end= ' ')
# 0 1 2 3 5 6 7 8 9