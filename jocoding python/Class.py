# # # Class란 ? 반복되는 변수 &메서드(함수)를 미리 정해놓은 틀(설계도) # # #

# result = 0
# def add(num):
#     global result
#     result += num
#     return result 

# print(add(3))
# print(add(4))



# class calculator:
#     def __init__(self):
#         self.result = 0

#     def add(self, num):
#         self.result += num
#         return self.result

# cal1 = calculator()
# cal2 = calculator()

# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))

# class Fourcal:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
#     def mul(self):
#         result = self.first * self.second
#         return result
#     def sub(self):
#         result = self.first - self.second
#         return result
#     def div(self):
#         result = self.first / self.second
#         return result
# class SafeFourcal(Fourcal):
#     def div(self):
#         if self.second == 0:
#             return 0
#         else:
#             return self.first / self.second

# class MoreFourcal(Fourcal):
#     def pow(self):
#         result = self.first ** self.second
#         return result

# a = Fourcal(4,0)
# print(a.div())

# class Family:
#     lastname = "kim"

# Family.lastname = "park"
# print(Family.lastname)

# a = Family()
# b = Family()
# print(a.lastname)
# print(b.lastname)


### moudule? 미리 만들어 놓은 Py파일(함수, 변수, 클래스)


### 예외처리
# try
# except Exception as e:
# else
# final

# try :
#     4/0
# except ZeroDivisionError as e:
#     print(e)    
#     print("hihi")

# f = open('foo.txt', 'w')
# try:
#     # 무언가를 수행한다.
#     data = f.read()
#     print(data)
# except Exception as e:  ### Exception은 모든 오류 처리 가능!!
#     print(e)
# finally:
#     f.close()
    

# class Bird:
#     def fly(self):
#         raise NotImplementedError

# class Eagle(Bird):
#     def fly(self):
#         print("very fast")

# eagle = Eagle()
# eagle.fly( )