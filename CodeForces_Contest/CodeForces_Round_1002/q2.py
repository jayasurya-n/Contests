from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        n,k = list(map(int,input().strip().split()))
        nums = list(map(int,input().strip().split()))
        
        if(n==k):
            for i in range(1,n,2):
                if(nums[i]!=(i+1)//2):return (i+1)//2
            return k//2+1

        for i in range(1,n-k+2):
            if(nums[i]!=1):return 1
        return 2
        
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)