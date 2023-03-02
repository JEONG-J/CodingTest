n = int(input())
num = list(map(int, input().split()))

num.reverse()

for i in range(n):
	print(num[i], end = ' ')
