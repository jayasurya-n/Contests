from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        n,m = list(map(int,input().strip().split()))
        arr = []
        for _ in range(n):
            arr.append(list(map(int,input().strip().split())))
        
        arr.sort(key=lambda x:sum(x),reverse=True)
        
        tsum = curr = 0
        for i in range(n):
            for j in range(m):
                curr+=arr[i][j]
                tsum+=curr
        return tsum

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)