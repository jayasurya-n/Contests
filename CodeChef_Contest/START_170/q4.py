from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        arr.sort(reverse=True)
        ans = max(sum(arr),n**2)
        curr = 0
        for i in range(n):
            curr+=arr[i]
            ans = max(ans,curr+(n-1-i)**2)
        return ans
    
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)