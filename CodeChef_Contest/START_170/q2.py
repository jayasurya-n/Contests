from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        n,x = list(map(int,input().strip().split()))
        arr = list(map(int,input().strip().split()))
        arr.sort(reverse=True)
        
        ans = arr[0]
        increment=x
        for i in range(1,len(arr)):
            ans = max(ans,arr[i]+increment)
            increment+=x
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)