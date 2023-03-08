n = int(input())

students = []
for _ in range(n):
    data = input().split()
    students.append((data[0],int(data[1])))

# 키를 이용하여 점수를 기준으로 정렬
students.sort(key=lambda students: students[1])

for student in students:
    print(student[0], end = ' ')