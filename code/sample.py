# factorial.py
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example
print(factorial(5))

# fibonacci.py
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Example
print(fibonacci(7))

# fibonacci-sequence.py
def fibonacci_sequence(n):
    a, b = 0, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Example
fibonacci_sequence(10)

#3_bool.py
a = true 
b= false
c= true
#숫자에서 boold로 변환
d= bool(0)
e=bool(1)
f=bool(-1)
g=bool(10)
h=bool("1")
i=bool("")
j= bool('heelo')
print(a,b,c,d,e,f,g,h,i,j)




3_list.py
#리스트 생성
my_list = [10,20,30,40]
#리스트 요소에 접근
print(my_list[0])
print(my_list[3])
#리시트에 요소 추가
my_list.append(50)

#특정 위치에 요소 삽입
my_list.insert(1,15)
print(my_list)

#리스트에서 요소 삭제
my_list.remove(30)
print(my_list)

#인덱스로 요소 삭제
delect my_list[2]
print(my_list)

#리스트 길이 구하기
print(len(my_list))

#리스트의 모든 요소 반복
for item in my_list:
print(item)

#리스트 슬라이싱
sub_list_1 = my_list[1:3]
print(sub_list)

for i in range(6,15, 2):
    my_list.append(i * 10)
    print(my_list)

sub list_2 = my_list[4:]
sub_list_3 = my_list[:4]
sub_list_4 = my_list[2:8:2]
sub_list_5 = my_list[::]

print(f"s2: {sub_list_2}")
print(f"s3: {sub_list_3}")
print(f"s4: {sub_list_4}")
print(f"s5: {sub_list_5}")

