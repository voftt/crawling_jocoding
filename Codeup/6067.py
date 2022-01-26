a = int(input())


if (a<0) and (a%2==0):
    print('A')
if (a<0) and (a%2!=0):
    print('B')
if (a>0) and (a%2==0):
    print('C')
if (a>0) and (a%2!=0):
    print('D')

n = int(input())

if n<0:
    if n%2==0:
        print('A')
    else:
        print('B')
else:
    if n%2==0:
        print('C')
    else:
        print('D')