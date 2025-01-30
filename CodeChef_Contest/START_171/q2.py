from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        m,k = list(map(int,input().strip().split()))
        s = input().strip()
        
        swish = 0
        for ch in s:
            if(ch=='S'):swish+=1
        
        if(swish>=k):return len(s)
        return len(s)+k-1-swish

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)