
# Study1))
# 별짓기
# 반복문 조건문 이용
# 출력:
#     * 1
#     ** 2
#     **** 4
#     ***** 5
#     ******* 7 
#     ******** 8

star = '*'
for x in range(1,9) :
    if x == 3 or x== 6:
        continue
    print(star * x)
    


print()
print()
# Study2))
# 다음은 map함수에 대한 설명이다. map 함수와 lambda 함수를 이용하여, 10진수 숫자가 문자열로 작성된 리스트 a의 각 원소의 값을 1씩 증가시킨 문자열로 변경하는 프로그램을 한 줄의 코드로 작성하시오.

# map(func, iter) 함수는 두 개의 입력을 받는다.
# 첫 번째 입력 func은 하나의 입력을 받는 함수이며, 반드시 출력이 존재한다.
# map 함수는 두 번째 입력 iter를 순회하면서 각 원소 elem을 func의 입력으로 하여, func(elem)을 출력하는 iterative object를 출력한다.
# map의 출력은 일회성으로 동작하는 iterative object이며, list() 또는 tuple()을 이용하여 여러번 참조할 수 있도록 변환할 수 있다.

# a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# <이곳에 들어갈 한 줄의 코드를 작성>
# print(a)

# 예상 출력 : ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
a = list(map(str,list(map(lambda x : int(x)+1, a))))
print(a)
b = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
b = list(map(lambda x : int(x)+1, b))
print(b)



print()
print()
# Study3))
a = ['soccer', 'basket ball', 'base ball', 'basket ball', 'tennis']

basketBallCount = a.count("basket ball")
baseBallCount = a.count("base ball")
soccerCount = a.count("soccer")
print("basket ball", basketBallCount)
print("base ball", baseBallCount)
print("soccer", soccerCount)



print()
print()
# Study4))
# print()
# 예상 출력 : 0 1 2 4 8 16 32 64 128 256 256 256

p=1;
numList=None
for i in range(-1,11):
    if i == -1:
        print(0,end=' ')
    elif i < 8:
        print(p,end=' ')
        p=p*2;
    else:
        print(p,end=' ');
