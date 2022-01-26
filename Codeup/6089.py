# a, d, n = input().split()
# a = int(a)
# d = int(d)
# n = int(n)



# mul = a*d**(n-1) 

# print(mul)

a, r, n = input().split()

a = int(a)
r = int(r)
n = int(n)

for i in range(1, n) :
  a = a*r

print(a)

