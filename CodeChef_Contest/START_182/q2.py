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
        n,k,D = lii()
        t = lii()
        pq = [(t[i],i) for i in range(n)]
        heapq.heapify(pq)
        
        waiting = [] 
        ans = 0
        for day in range(1,D+1):
            while waiting and waiting[0][0]<=day:
                _,ti,i = heapq.heappop(waiting)
                heapq.heappush(pq,(ti,i)) 
                
            while len(pq)>k:
                ti,i = heapq.heappop(pq)
                heapq.heappush(waiting,(day+ti,ti,i))
                ans+=1
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)