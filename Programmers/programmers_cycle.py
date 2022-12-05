dxy = [[1,0],[0,-1],[-1,0],[0,1]]

def solution(grid):
    global visited,n,m
    n = len(grid)
    m = len(grid[0])
    visited = [[[False]*4 for _ in range(m)] for _ in range(n)]    
    answer = []
		
    for cx in range(n):
        for cy in range(m):
            for cd in range(4):
                if not visited[cx][cy][cd]:
                    cycle = simul(grid,cx,cy,cd)
                    if cycle != 0:
                        answer.append(cycle)
    answer.sort()
    return answer

def simul(grid,cx,cy,cd):
    x,y,d = cx,cy,cd
    cnt = 0
    visited[cx][cy][cd] = True
    while True:
        x = (x + dxy[d][0]) % n
        y = (y + dxy[d][1]) % m
        cnt += 1

        if grid[x][y] == 'R':
            d = (d+1) % 4
        elif grid[x][y] == 'L':
            d = (d-1) % 4
        if visited[x][y][d]:
            if (x,y,d) == (cx,cy,cd):
                return cnt
            else:
                return 0
        visited[x][y][d] = True
