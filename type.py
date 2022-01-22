# # a = 4.24e10

# # print(a)


# # 튜플 : 소괄호, 변경 불가능 vs 리스트 : 대괄호, 변경 가능 
# t1 = (1,2,'a','b')
# print(t1[0])
# print(t1[0:2])

# t2= (4,5)
# print(t1 + t2)
# print(t1*3)


# #딕셔너리(=Associative array=Hash), key를 통해 value 얻음

# a = {1 : 'a'}
# a['name'] = '익명'

# del a[1] #key를 건드려야함

# print(a)

# a = {1 : '파랑구름', 2: '이현준', 3:'정현준'}

# print(a.keys())
# print(a.values())
# print(a.items())
# a.clear()
# print(a)
# print(a[4])
# print(a.get(4,"없음"))
# print(4 in a)
# print(1 in a) 

# # 집합 자료형 
# s1 = set([1,2,3])
# s1 = {1,2,3}
# print(s1)

# l = [1,2,2,3,3,4]
# newlist = list(set(l))
# print(newlist)

# s2= set("hello")
# print(s2)


# s1 = set([1,2,3,4,5,6])
# s2 = set([4,5,6,7,8,9])
# # 교집합
# print(s1 & s2)          
# print(s1.intersection(s2))
# # 합집합
# print(s1 | s2)
# print(s1.union(s2))
# # 차집합
# print(s1 - s2)
# print(s1.difference(s2))

# s1.add(7)
# print(s1)
# s1.update([7,8,9])
# print(s1)
# s1.remove(1)
# print(s1)

# # 불(bool)  :true false
# a = True # 대문자로 써야함 
# b = False
# print(type(a))
# print(type(b))

# a = [1,2,3,4]
# while a:
#     a.pop() #pop은 마지막 요소를 없앰
#     print(a)

###  주소를 가져온 것이기 때문에 동일(포인터개념)
# a = [1,2,3]
# b = a ### b에 a라는 주소가 넣어진 것 
# a[1] = 5
# print(id(a))
# print(id(b))
# print(a is b)

# b = a[:] ### b에 새로운 리스트를 넣는 것 
# a[1] = 4
# print(id(a))
# print(id(b)) 

# a, b = ('python', 'life')
# (a, b) = ('python', 'life')
# (a, b) = 'python', 'life'

# print(a)
# print(b)

# c = d = 'hello'
# print(c)
# print(d)

# # 다른 언어 swap 과정
# a = 3
# b = 5
# tmp = b
# b = a 
# a = tmp
# print(a)
# print(b)

a=3
b=5
a,b=b,a
print(a)
print(b)
