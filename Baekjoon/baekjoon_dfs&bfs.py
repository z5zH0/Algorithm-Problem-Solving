from collections import deque

n, m, v = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
	a, b = map(int, input().split())
	graph[a][b] = graph[b][a] = 1
	
dfs_visited = [0] * (n + 1)
bfs_visited = [0] * (n + 1)
	
def dfs(v):
	dfs_visited[v] = 1
	print(v, end=" ")
	
	for i in range(n+1):
		if graph[v][i] == 1 and dfs_visited[i] == 0:
			dfs(i)

def bfs(v):
	queue = deque([v])
	bfs_visited[v] = 1
	while queue:
		v = queue.popleft()
		print(v, end=" ")
		for i in range(n+1):
			if graph[v][i] == 1 and bfs_visited[i] == 0:
				queue.append(i)
				bfs_visited[i] = 1
		
dfs(v)
print()
bfs(v)
