from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        m,n = list(map(int,input().strip().split()))
        grid = []
        for _ in range(m):grid.append(list(input().strip()))
        
        start,end = None,None
        for i in range(m):
            for j in range(n):
                if(grid[i][j]=='S'):start = (i,j)
                elif(grid[i][j]=='G'):end = (i,j)
        
        q = deque([(start[0],start[1],0,-1)])
        visited = [[False]*n for _ in range(m)]
        visited[start[0]][start[1]] = True
        
        while q:
            i,j,d,odir = q.popleft()
            if((i,j)==end):return d
            
            moves = [[(1,0),(-1,0)],[(0,1),(0,-1)]]
            directions = []
            if(odir==-1):directions = [0,1]
            elif(odir==0):directions = [1]
            elif(odir==1):directions = [0]
            
            for dir in directions:
                for dx,dy in moves[dir]:
                    ni,nj = i+dx,j+dy
                    if(0<=ni<m and 0<=nj<n and not visited[ni][nj] and grid[ni][nj]!='#'):
                        q.append((ni,nj,d+1,dir))
                        visited[ni][nj] = True
        return -1
                
if __name__ == "__main__":
    # N = 2*(10**5)+5
    # mod = 10**9+7
    # fac = [1]*N
    # for i in range(1,N):
    #     fac[i] = (fac[i-1]*i)%mod
    yes = "YES"
    no = "NO"
    for _ in range(1):
        ans = Solution().run()
        print(ans)