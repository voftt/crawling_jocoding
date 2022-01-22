import re   
p = re.compile("[a-z]+")
m = p.match("python")
print(m)

n = p.search("python")
print(n)

