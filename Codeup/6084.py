h, b, c, s = input().split()
h = int(h)
b = int(b)
c = int(c)
s = int(s)

sound = h*b*c*s/8/1024/1024

print(format(sound,".1f"),"MB")
