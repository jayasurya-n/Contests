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
        n,s,x = lii()
        arr = lii()

        def count(arr,s,x):
            ans = 0
            hash = defaultdict(int)
            hash[0^seed] = 1
            csum = 0
            for num in arr:
                if(num>x):
                    hash = defaultdict(int)
                    hash[0^seed] = 1
                    csum = 0
                else:
                    csum+=num
                    ans+=hash[(csum-s)^seed]
                    hash[csum^seed]+=1
            return ans
        
        return count(arr,s,x)-count(arr,s,x-1)

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)