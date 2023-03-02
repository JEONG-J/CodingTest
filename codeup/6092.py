n = int(input())
num = list(map(int, input().split()))
res = []
cnt = 0

for _ in range(24):
	res.append(0)

for i in range(n):
	res[num[i]] += 1

for i in range(1, 24):
	print(res[i], end = ' ')
