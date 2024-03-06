board = []
for _ in range(5):
    board.append(list(map(int, input().strip().split())))

speak = []
for _ in range(5):
    speak.append((list(map(int, input().strip().split()))))

bingo = [[0] * 5 for _ in range(5)]

def check_row():
    result = 0
    for x in range(5):
        cnt = 0
        for y in range(5):
            if bingo[x][y] == 1:
                cnt += 1
        if cnt == 5:
            result += 1
    return result

def check_col():
    result = 0
    for x in range(5):
        cnt = 0
        for y in range(5):
            if bingo[y][x] == 1:
                cnt += 1
        if cnt == 5:
            result += 1
    return result

def check_dia():
    result = 0
    cnt = 0
    for x in range(5):
        if bingo[x][x] == 1:
            cnt += 1
    if cnt == 5:
        result += 1

    cnt = 0
    for x in range(5):
        if bingo[x][5-x-1] == 1:
            cnt += 1
    if cnt == 5:
        result += 1

    return result

result_list = []

for x in range(5):
    for y in range(5):
        s = speak[x][y]
        for a in range(5):
            for b in range(5):
                if board[a][b] == s:
                    cnt = 0
                    bingo[a][b] = 1
                    cnt += check_row()
                    cnt += check_col()
                    cnt += check_dia()
                    if cnt >= 3:
                        result_list.append(x * 5 + y + 1)

print(result_list[0])