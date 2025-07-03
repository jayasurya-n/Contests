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
        value = lii()

        mark = [0]*(n+1)
        for num in value:mark[num] = 1

        missing = [i for i in range(1,n+1) if mark[i]==0]
        
        adj = [[] for _ in range(n)]
        for _ in range(n-1):
            u,v = lii()
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        
        ans = n+1
        for u in range(n):
            maxi = cnt = 0
            if(value[u]>0):
                for v in adj[u]:
                    maxi = max(maxi,value[v])
                    if(value[v]==0):cnt+=1
                
                if(maxi<value[u]):
                   if(cnt==0 or  missing[cnt-1]<value[u]):
                    ans = min(ans,value[u])
            else:
                cnt+=1
                for v in adj[u]:
                    maxi = max(maxi,value[v])
                    if(value[v]==0):cnt+=1
                
                ind = bisect.bisect_right(missing,maxi)
                if(ind==len(missing)):continue

                ans = min(ans,max(missing[cnt-1],missing[ind]))
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)