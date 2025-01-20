from typing import List,Optional
from collections import deque
import sys, heapq
from math import ceil, floor, gcd, sqrt, log

def nCr(n,r):VVVVVVVVVVVVVVVV
    if(n<r or n<0 or r<0):return 0
    return fac[n]*pow(fac[r],mod-2,mod)*pow(fac[n-r],mod-2,mod)

class Solution:
    def run(self):
        n,m,k = list(map(int,input().strip().split()))
        w = int(input().strip())
        heights = list(map(int,input().strip().split()))
        
        heights.sort(reverse=True)
    
        grid = [[0]*m for _ in range(n)]
        
        center_x = (n - 1) // 2
        center_y = (m - 1) // 2
        
        heap = []
        for i in range(n):
            for j in range(m):
                distance = abs(i - center_x) + abs(j - center_y)
                heapq.heappush(heap, (distance, i, j))
        
        idx = 0
        while heap and idx < len(heights):
            _, i, j = heapq.heappop(heap)
            grid[i][j] = heights[idx]
            idx += 1

        p = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                p[i][j] = (grid[i-1][j-1] +
                                        p[i-1][j] +
                                        p[i][j-1] -
                                        p[i-1][j-1])
        
        ans = 0
        for i in range(k, n + 1):
            for j in range(k, m + 1):
                s = (p[i][j] -
                                p[i-k][j] -
                                p[i][j-k] +
                                p[i-k][j-k])
                ans += s
        print(ans)
    

            
            
            
        
if __name__ == "__main__":
    # N = 2*(10**5)+5
    # mod = 10**9+7
    # fac = [1]*N
    # for i in range(1,N):
    #     fac[i] = (fac[i-1]*i)%mod
    for _ in range(int(input().strip())):
        Solution().run()