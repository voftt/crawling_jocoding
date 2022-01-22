# # # 함수 # # #
# def 함수명(매개변수(inputx))
#     <수행 문장1>
#     <수행 문장2>
#     ...
#     return 리턴 값(outputf(x))

# def sum(a,b):
#     result = a+b
#     return result
# print(sum(1,2))

# def sum_and_mul(a,b):
#     return a+b, a*b, a-b

# print(sum_and_mul(1,2))

# def say_myself(name, old, man=True):
#     print("나의 이름은 %s 입니다." % name)
#     print("나이는 %d살입니다." % old)
#     if man:
#         print("남자입니다.")
#     else:
#         print("여자입니다.")
# say_myself("김주형", 15,)
# say_myself("박응용", 27, True)

## 효력 범위 ##
# a = 1
# def vartest(a):
#     a = a + 1
#     return a

# a = vartest(a)
# print(a)

# a = 1
# def vartest():
#     global a
#     a = a+1

# vartest()
# print(a)

# def add(a,b):
#     return a+b

# add = lambda a, b: a+b
# print(add(1,2))


# mylist = [lambda a,b: a+b, lambda a,b: a*b]
# print(mylist[1](1,2))



# # 입력과 출력 # #

# number = input("숫자 입력해")

# print(number)    

# for i in range(10):
#     print(i, end="and")

# # # 파일 읽고 쓰기 # # 
# f = open("새파일.txt", 'w', encoding="UTF-8")
# for i in range(1,11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# f= open("새파일.txt", 'r', encoding="UTF-8")
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

# f= open("새파일.txt", 'r', encoding="UTF-8")
# while True:
#     lines = f.readlines()
#     for line in lines:
#         print(line, end="") # print(line.strip("\n"))
# f.close()

# f=open("새파일.txt", 'r', encoding="UTf-8")
# data = f.read()
# print(data)
# f.close()