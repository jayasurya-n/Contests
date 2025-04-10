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
        n = ii()
        p = lii()
        
        adj = [[] for _ in range(n)]
        ans = []
        cnt = 0
        for i in range(n-1):
            u,v = p[i]-1,i+1
            adj[u].append(v)
            
            if(u==0):
                if(len(adj[u])%2==1 and len(adj[u])!=1):cnt-=1
                elif(len(adj[u])%2==0):cnt+=1
            else:
                if(len(adj[u])%2==0):cnt-=1
                else:cnt+=1
            
            if(cnt>0 or i%2==1):ans.append('0')
            else:ans.append('1')
        
        print("".join(ans))
        if(ans[-1]=='0'):return

        hash = [-1]*n
        color = 1
        for u in range(n):
            start = 0
            if(u==0):
                hash[u] = color
                hash[adj[u][0]] = color
                start = 1
            
            for j in range(start,len(adj[u]),2):
                color+=1
                hash[adj[u][j]] = color
                hash[adj[u][j+1]] = color                 
        
        print(*hash)           

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()