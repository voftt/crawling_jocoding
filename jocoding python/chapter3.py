# # # 조건문 # # #
# money = 2000
# card = 1
# if False or True : # or = |
#     print("taxi")
# else :
#     print("walk")

#     money = 2000
# card = 1
# if False or True : # or = |
#     print("taxi")
# else:
#     print("걸어가")

# pocket = ['paper', 'cellphone']
# card = False
# credit = True
# if 'money' in pocket:
#     pass
# elif card:
#     print("택시")
# elif credit:
#     print("느그서장이랑임마")
# else:
#     print("걸어가라")

# score = 70
# if score >= 60:
#     message = "suc"
# else:
#     message = "fail"
# print(message)
# 
# score = 70
# message="suc" if score>=60 else "fail"
# print(message)



# # # 반복문 # # #
# # while # #
# treehit = 0
# while treehit < 10:
#     treehit = treehit +1
#     print("나무를 %d번 찍었습니다." %treehit)
#     if treehit == 10:
#         print("나무가 넘어갑니다.")


# coffee = 10
# money = 3000
# while money:
#     print("돈을 받았으니 커피를 줍니다.")
#     coffee = coffee-1
#     print("남은 커피는 %d개입니다." %coffee)
#     if not coffee : 
#         print("커피가 다 떨어졌습니다.")
#         break

# a = 0
# while a < 10:
#     a = a+1
#     if a % 2 == 0:
#         continue
#     print(a)

# while True:
#     print("안녕하세요")



# # for # # 
# test_list = ['one', 'two', 'three']
# for i in test_list:
#     print(i)

# marks = [90, 25, 67, 45, 80]
# number = 0
# for mark in marks:
#     number = number +1
#     if mark >= 60:
#         print("%d번 학생은 합격" %number)
#     else:
#         print("%d번 학생은 불합격" %number)

# for mark in marks:
#     number = number+1
#     if mark < 60: continue
#     print("%d번 학생 축하합니다. 합격입니다!" % number)


# sum = 0
# for i in range(1, 11):
#     sum = sum + i
# print(sum)

# for i in range(2,10):
#     for j in range(1, 10):
#         print(i*j,end=" " )
#     print("")