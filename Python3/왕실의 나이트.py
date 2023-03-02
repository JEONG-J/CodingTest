n = input() # 1자리 열, 2자리 행
row = int(n[1])
col = int(ord(n[0])) - int(ord('a')) + 1
res = 0

dirs = [(2,1), (1,2), (-2,1), (1,-2), (2,-1), (-1,2), (-1,-2), (-2,-1)]

for dir in dirs:
    newRow = row + dir[0]
    newCol = col + dir[1]
    if newRow >= 1 and newRow <= 8 and newCol >= 1 and newRow <= 8:
        res += 1

print(res)