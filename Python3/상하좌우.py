n = int(input())
plans = input().split()
x, y = 1, 1
dx = [-1,1,0,0]
dy = [0,0,-1,1]
dir = ['L','R','U','D']

for plan in plans:
    for i in range(len(dir)):
        if plan == dir[i]:
            nx = x + dy[i]
            ny = y + dx[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)