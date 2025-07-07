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
        n,k = lii()
        positions = lii()
        delays = lii()

        # i,t,dir: n*k*2 states
        ans = [[[False]*2 for _ in range(k)] for _ in range(n)]
        q = deque([])

        for t in range(k):
            if(t==delays[0]):
                ans[0][t][1] = True
            else:
                q.append((0,t,0))
                ans[0][t][0] = True
        
        for t in range(k):
            if(t==delays[n-1]):
                ans[n-1][t][0] = True
            else:
                q.append((n-1,t,1))
                ans[n-1][t][1] = True
        
        while q:
            i,t,dir = q.popleft()
            # prev light
            if((dir==1 and i==0) or 
               (dir==0) and i==n-1):continue

            if(dir==1):
                nt = k+t-(positions[i]-positions[i-1])%k
                nt%=k
                if(nt==delays[i-1]):dir = 1-dir
                if(ans[i-1][nt][dir]==False):
                    q.append((i-1,nt,dir))
                    ans[i-1][nt][dir] = True
            
            else:
                nt = k+t-(positions[i+1]-positions[i])%k
                nt%=k
                if(nt==delays[i+1]):dir = 1-dir
                if(ans[i+1][nt][dir]==False):
                    q.append((i+1,nt,dir))
                    ans[i+1][nt][dir] = True
        
        l = ii()
        queries = lii()
        for pos in queries:
            ind = bisect.bisect_left(positions,pos)
            if(pos<positions[0] or pos>positions[-1]):
                print(yes)
                continue

            t = positions[ind]-pos
            t%=k
            print(yes if ans[ind][t][1] else no)


if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()