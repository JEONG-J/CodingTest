r, g, b = map(int, input().split())
cnt = 0

for x in range(r):
	for y in range(g):
		for z in range(b):
			print(x, y, z)
			cnt += 1
print(cnt)
