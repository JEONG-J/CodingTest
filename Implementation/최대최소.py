import sys

cnt = int(sys.stdin.readline())
for _ in range(int(cnt)):
    input_Data = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    print(min(data), max(data))