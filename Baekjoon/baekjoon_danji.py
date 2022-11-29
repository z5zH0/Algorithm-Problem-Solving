n = int(input())
graph = [] #2차원 리스트
danji = [] #단지내 집의 수를 저장할 리스트
for i in range(n):
	graph.append(list(map(int,input())))
	
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1] #위쪽부터 시계방향

visited = [[0]*n for _ in range(n)] #방문여부 체크

def dfs(x,y):
	global num #집의 수
	visited[x][y] = 1
	if graph[x][y] == 1:
		num += 1
	for i in range(4):
		cx = x + dx[i]
		cy = y + dy[i]
		if  0 <= cx < n and 0 <= cy < n: #그래프의 범위를 벗어나지 않는 선에서 네 방향으로 dfs
			if visited[cx][cy] == 0 and graph[cx][cy] == 1:
				dfs(cx,cy)
				
for i in range(n):
	for j in range(n):
		if graph[i][j] == 1 and visited[i][j] == 0:
			num = 0
			dfs(i,j)
			danji.append(num)

danji.sort()
print(len(danji))
for i in danji:
	print(i)
