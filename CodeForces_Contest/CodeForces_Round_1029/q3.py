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
        arr = lii()

        if(n==1):return 1

        ans = 1
        prev_hash = set()
        prev_hash.add(arr[0]^seed)

        curr_hash = set()
        for i in range(1,n):
            curr_hash.add(arr[i]^seed)
            if(arr[i]^seed in prev_hash):
                prev_hash.remove(arr[i]^seed)

            if(len(prev_hash)==0):
                ans+=1
                prev_hash = curr_hash
                curr_hash = set()

        return ans 

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)