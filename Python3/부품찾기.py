import time
import datetime
start_time = time.time()

# 계수 정렬활용
n = int(input())

array = [0] * 1000001
for i in input().split():
    array[int(i)] = 1 # 해당위치 값 1로 변경

data = int(input())
num = list(map(int,input().split()))

for i in num:
    if array[i] == 1:
        print("yes", end = ' ' )
    else:
        print("no", end = ' ')

print()
end_time = time.time()

sec = (end_time - start_time)
result = datetime.timedelta(seconds=sec)
print(result)



'''
# 이진탐색을 활용한 풀ㅣ
n = int(input())
inputData = list(map(int,input().split()))
m = int(input())
searchData = list(map(int,input().split()))

def binary(array, target, start, end):
    if start > end:
        print("no", end = ' ')
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        print("yes", end = ' ')
    elif array[mid] > target:
        return binary(array, target, start, mid-1)
    else:
        return binary(array, target, mid+1, end)
    
inputData.sort()
for i in searchData:
    binary(inputData, i, 0, n-1)
'''