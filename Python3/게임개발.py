n, m = map(int, input().split())
x, y, dir = map(int, input().split())

d = [[0] * m for _ in range(n)]
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int,input().split())))

dx = [-1, 0 ,1 ,0]
dy = [0,1,0,-1]

def turn():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3

cnt = 1
turn_cnt = 0
while 1:
    turn()
    nx = x + dx[dir]
    ny = y + dy[dir]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        cnt += 1
        x = nx
        y = ny
        turn_cnt = 0
    else:
        turn_cnt += 1
    if turn_cnt == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_cnt = 0

print(cnt)