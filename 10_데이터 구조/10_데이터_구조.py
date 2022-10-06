# 10_데이터 구조

# 10.2 순서가 있는 데이터

# 10.2.1 문자열

word = 'ym'
print(word) # ssafy
print(id(word)) # 메모리 주소 확인 2396061825776
word = 'ym2'
print(word) # test
print(id(word)) # 메모리 주소 확인 2396061825840

# 변수 안에 주소만 들어간다.

print('abcde'.find('b')) # 1
print('qwerty'.find('k')) # -1

print('xyz'.index('y')) # 1
# print('xyz'.index('k')) # Error

print('abc'.isalpha()) # True
print('ㄱㄴㄷ'.isalpha()) # True
print('Ab'.isupper()) # False
print('ab'.islower()) # True
print('Title Title!'.istitle()) # True

print('ooooo'.replace('o', 'a')) # aaaaa
print('xooxo'.replace('o', '!', 2)) # x!!xo

print('     대박!\n'.strip()) # '대박!'
print('     대박!\n'.lstrip()) # '대박!'
print('     대박!\n'.rstrip()) # '     대박!'
print('대박????'.rstrip('?')) # '대박'

print('a, b, c'.split('_')) # ['a, b, c']
print('a. b. c'.split('.')) # ['a', ' b', ' c']
print('a b c'.split()) # ['a', 'b', 'c']

# 주의!
a = 'h e l l o'
a.split() # ['h', 'e', 'l', 'l', 'o']
print(a) # 'h e l l o'

b = a.split()
print(b) # ['h', 'e', 'l', 'l', 'o']

print('!'.join('123456')) # '1!2!3!4!5!6'
print(' '.join(['3', '5', '7'])) # '3 5 7'