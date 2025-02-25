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
        n = ii()
        graph = []
        for _ in range(n):graph.append(si())
        ans = [[sys.maxsize]*n for _ in range(n)]
                
        q = deque([])
        for i in range(n):
            ans[i][i] = 0
            q.append((i,i))
            
        for i in range(n):
            for j in range(n):
                if(i==j or graph[i][j]=='-'):continue
                ans[i][j] = 1
                q.append((i,j))
        
        while q:
            u,v = q.popleft()
            d = ans[u][v]
            for i in range(n):
                for j in range(n):
                    if(graph[i][u]!='-' and graph[v][j]!='-' and 
                       graph[i][u]==graph[v][j]):
                        if(ans[i][j]>d+2):
                            ans[i][j] = d+2
                            q.append((i,j))
        
        for i in range(n):
            for j in range(n):
                if ans[i][j] == sys.maxsize:
                    ans[i][j] = -1
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(1):
        ans = Solution().run()
        for row in ans:print(*row)