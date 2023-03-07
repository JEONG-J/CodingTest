n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def change(a, b, cnt):
    a.sort()
    b.sort(reverse=True)

    for i in range(cnt):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break
    
    return sum(a)

print(change(a,b,m))
