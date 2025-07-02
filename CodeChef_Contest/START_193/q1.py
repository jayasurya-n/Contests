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
        odd = even = 0
        i = 1

        while i*i<=n:
            if(n%i==0):
                odd+=1 if i%2==1 else 0
                even+=1 if i%2==0 else 0
                if(i*i!=n):
                    odd+=1 if (n//i)%2==1 else 0
                    even+=1 if (n//i)%2==0 else 0
            i+=1
        
        return [odd,even]


if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(*ans)