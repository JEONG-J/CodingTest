n, m = map(int,input().split()) # 떡의 개수와 요청한 떡의 길이를 입력받기
array = list(map(int,input().split())) # 떡의 높이 정보 입력 받기

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in array:
        if i > mid: # 잘랐을 떄 떡의 양
            total += i - mid
    if total < m: # 떡의 양 부족한 경우 더 자르기
            end = mid - 1
    else:
        result = mid # 떡의 양이 충분한 경우 덜 자르기 and 덜 잘랐을 때가 정답!!
        start = mid + 1

print(result)