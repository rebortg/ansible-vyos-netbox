import sys

a = sys.argv[1]
print(sys.argv)

config = {}
new = []
a = a.replace("'","")
for i in a.split('\n'):
    new.append(i.split(' '))

for n in new:
    i = 0
    c = config
    for e in n:
        if i+2 == len(n):
            c[e] = n[i+1]
            break
        if e in c.keys():
            c = c[e]
        else:
            c[e] = {}
            c = c[e]

        i += 1
        

print(config)