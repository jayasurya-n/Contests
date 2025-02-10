from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        n = int(input().strip())
        degrees = [0]*n
        adj = [[] for _ in range(n)]
        for _ in range(n-1):
            u,v = list(map(int,input().strip().split()))
            u-=1
            v-=1
            adj[u].append(v)
            adj[v].append(u)
            degrees[u]+=1
            degrees[v]+=1
        
        ans = 1
        sdegrees = sorted([(degrees[i],i) for i in range(n)],reverse=True)
        first = []
        for i in range(n):
            if(sdegrees[i][0]==sdegrees[0][0]):first.append(sdegrees[i][1])
            else:break
        
        if(len(first)==1):
            f = sdegrees[0][1]
            ans+=sdegrees[0][0]-1
            for v in adj[f]:
                degrees[v]-=1
                degrees[f]-=1
            return ans+max(degrees)-1
        
        else:
            adjacent = True
            hash = set(first)
            for f in first:
                cnt = 0
                for v in adj[f]:
                    if(v in hash):cnt+=1
                if(cnt<len(first)-1):adjacent = False
            return ans+2*sdegrees[0][0]-(2 if not adjacent else 3)

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)