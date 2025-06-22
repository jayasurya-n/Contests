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
        m = ii()
        ope = lii()
        
        # inv = cross = 0
        # n = 1
        # ans = []
        
        # for i in range(m):
        #     if(ope[i]==1):
        #         inv+=n
        #         cross+=n
        #         n+=1
        #     else:
        #         inv=2*inv+cross
        #         cross*=4
        #         n*=2
        #     ans.append(inv)
        # return ans

        c1 = c2 = 0
        n = 1
        ans = []
        for i in range(m):
            if(ope[i]==1):
                c2+=n
                n+=1
            else:
                nc1=3*c1+c2
                nc2=3*c2+c1
                c1,c2 = nc1,nc2
                n*=2
            ans.append(c2)
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(*ans)