### Immutable ###
a = 1 # 전역변수 
def vartest(a): # 지역변수
    a = a+1
vartest(a)
print(a)

### mutable ###
b = [1,2,3]
def vartest2(b):
    b=b.append(4)
vartest2(b)
print(b)