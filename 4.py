A = float(input("A = "))

while A < 0 or A > 50:
	A = float(input("A = "))

sumProb = start
count = 0

while sumProb < 200:
	sumProb += sumProb * (A / 100) 
	count += 1

print(sumProb)
print(count)