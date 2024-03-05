n = int(input())

cnt = 0
cows = {}
for i in range(n):
    cow, location = map(int, input().split())
    if cow not in cows:
        cows[cow] = location
    elif cows[cow] != location:
        cows[cow] = location
        cnt += 1

print(cnt)