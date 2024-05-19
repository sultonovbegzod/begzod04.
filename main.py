A = int(input(" A "))
B = int(input(" B "))

while A > B:
	A = int(input(" A "))
	B = int(input(" B "))

S = 1

for i in range(A,B+1):
	print(i)
	S *= i

print(S)