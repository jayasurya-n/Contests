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
        arr = lii()

        min_heap = []
        cnt = 0
        for num in arr:
            cnt+=bin(num).count('1')
            for i in range(61):
                bit = 1 if (num>>i)&1>0 else 0
                if(bit==1):continue
                heapq.heappush(min_heap,(1<<i))
        
        curr = new = 0
        while min_heap and curr+min_heap[0]<=k:
            curr+=heapq.heappop(min_heap)
            new+=1
        return cnt+new

                

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)