# 02_기초 문법

# 1. 들여쓰기

for i in range(10):
    print(i)  # 들여쓰기
    

# 2. 주석 / 3. 변수

# 추상화
print(20000 * 2 + 34000)

chicken = 20000
pizza = 34000

print(chicken)
print(chicken * 2 + pizza)

# 변수는 할당 연산자(=)를 통해 값을 할당
chicken = 20000
pizza = 34000

# 같은 값을 동시에 할당 가능
chicken = pizza = 30000
print(chicken, pizza)

# 다른 값을 동시에 할당 가능
chicken, pizza = 15000, 28000
print(chicken, pizza)


'''
각 변수의 값을 바꿔서 저장
'''

# 방법 1) 임시 변수
a, b = 100, 300
tmp = a
b = tmp
print(a, b)

# 방법 2) Pythonic!
a, b = 200, 400
a, b = b, a
print(a, b)