n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# dfs로 특정한 노드를 방문한 뒤에 연결된 모든 노드들 방문
def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

res = 0
for i in range(n):
    for z in range(m):
        if dfs(i,z) == True:
            res += 1

print(res)