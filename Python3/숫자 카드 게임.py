n, m = map(int, input().split())
res = 0

for i in range(m):
    data = list(map(int, input().split()))
    res = max(res, min(data))    

print(res)