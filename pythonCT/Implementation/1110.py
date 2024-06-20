num = int(input())
result = num
count = 0

while True:
    first = result // 10
    second = result % 10

    temp_one = first + second

    result = (second * 10) + (temp_one % 10)
    count += 1

    if result == num:
        break

print(count)