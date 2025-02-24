from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def run(self):
        n,m = lii()
        matrix = []
        for _ in range(n):matrix.append(lii())
        
        hash = [0]*(n*m+1)

        for i in range(n):
            for j in range(m):
                color = matrix[i][j]
                if(hash[color]==2):continue
                hash[color]=1
                for di,dj in [(0,1),(0,-1),(-1,0),(1,0)]:
                    ni,nj = i+di,j+dj
                    if(0<=ni<n and 0<=nj<m):
                        if(matrix[ni][nj]==color):hash[color] = 2
        
        return sum(hash)-max(hash)
    
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)