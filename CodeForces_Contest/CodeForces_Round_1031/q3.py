from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect, random
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def run(self):
        n,m,k = lii()
        grid = []
        for _ in range(n):
            grid.append(list(si()))
        
        prefix = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                prefix[i][j] = 1 if grid[i][j]=='g' else 0
                if(i>0):prefix[i][j]+=prefix[i-1][j]
                if(j>0):prefix[i][j]+=prefix[i][j-1]
                if(i>0 and j>0):prefix[i][j]-=prefix[i-1][j-1]

        ans = m*n+1
        gold = 0
        for i in range(n):
            for j in range(m):
                if(grid[i][j]=='g'):gold+=1
                if(grid[i][j]!='.'):continue
                i1 = max(i-(k-1),0)
                i2 = min(i+(k-1),n-1)

                j1 = max(j-(k-1),0)
                j2 = min(j+(k-1),m-1)

                count = prefix[i2][j2]
                if(i1>0):count-=prefix[i1-1][j2]
                if(j1>0):count-=prefix[i2][j1-1]
                if(i1>0 and j1>0):count+=prefix[i1-1][j1-1]
                ans = min(ans,count)
        
        return gold-ans


if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)