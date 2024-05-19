A = int(input(" A "))
N = int(input(" N "))

while N <= 0:
	N = int(input(" N "))

b = 1

for x in range(1,N+1):
	b = b * A

print(A,'^',N,'=',b)