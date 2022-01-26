n = int(input())
a = input().split()

for i in range(0,n):
    a[i]=int(a[i])

d = []
for i in range(0,24):
    d.append(0)

for i in range(0,n):
    d[a[i]]+=1
    
for i in range(1,24):
    print(d[i],end=" ")