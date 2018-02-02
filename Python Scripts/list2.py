a = []
r = int(input())
c = int(input())

for i in range(r):
    a.append([])
    for j in range(c):
	    t = int(input())
	    a[i] = a[i] + [t]
print(a)	    
