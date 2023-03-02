n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

res = 0
first = data[n-1]
second = data[n-2]

count = int(m/(k+1)) * k
count += m % (k+1)

res += first * count
res += second * (m-count)

print(res)