from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        n,q = list(map(int,input().strip().split()))
        positions = list(range(n))
        count = defaultdict(lambda:1)
        ans = 0
        for _ in range(q):
            query = list(map(int,input().strip().split()))
            if(query[0]==2):print(ans)
            else:
                _,p,h = query
                p-=1
                new_nest = h-1
                old_nest = positions[p]
                count[old_nest]-=1
                if(count[old_nest]==1):ans-=1
                
                positions[p] = new_nest
                count[new_nest]+=1
                if(count[new_nest]==2):ans+=1
                
                
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(1):
        ans = Solution().run()