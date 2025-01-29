from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        m,n = list(map(int,input().strip().split()))
        graph = []
        for _ in range(m):graph.append(list(input().strip()))
        
        if(graph[0][1]=='#' or graph[1][0]=='#'
           or graph[m-1][n-2]=='#' or graph[m-2][n-1]=='#'):return -1
        
        
        def bfs(graph,i,j,distance):
            q = deque([(i,j)])
            distance[i][j] = 0            
            while q:
                x,y = q.popleft()
                for dx,dy in [(0,1),(0,-1),(-1,0),(1,0)]:
                    nx,ny = x+dx,y+dy
                    if(0<=nx<m and 0<=ny<n and distance[nx][ny]==-1 and graph[nx][ny]=='.'):
                        distance[nx][ny] = 1+distance[x][y]
                        q.append((nx,ny))
            
        
        distance1 = [[-1]*n for _ in range(m)]
        distance2 = [[-1]*n for _ in range(m)]
        
        bfs(graph,0,0,distance1)
        bfs(graph,m-1,n-1,distance2)
        
        d = distance1[m-1][n-1]
        if(d==-1):return -1

        count = [0]*(m*n)
        for i in range(m):
            for j in range(n):
                if(graph[i][j]=='.' and distance1[i][j]!=-1):
                    d1 = distance1[i][j]
                    d2 = distance2[i][j]
                    if(d1+d2==d):count[d1]+=1
        
        for x in range(1,d):
            if(count[x]==1):return d+2
        return d

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)