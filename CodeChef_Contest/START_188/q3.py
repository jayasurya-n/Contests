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
        levels = lii()
        gold = lii()

        x = []
        for i in range(n):
            x.append((levels[i],gold[i],i))
        
        x.sort()
        ans = [0]*n

        pq = [x[0][1]]
        max_sum = x[0][1]
        for i in range(1,n):
            level,val,ind = x[i]
            ans[ind] = max_sum

            if(len(pq)<k):
                heapq.heappush(pq,val)
                max_sum+=val
            elif(pq[0]<val):
                last = heapq.heappop(pq)
                heapq.heappush(pq,val)
                max_sum+=val-last
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(*ans)