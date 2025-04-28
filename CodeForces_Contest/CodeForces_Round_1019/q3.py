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
        
        nums = []
        for num in arr:
            if(num>k):nums.append(-1)
            else:nums.append(1)
        
        # first, second
        # last,second
        # first, third
        def check(nums):
            psum = [0]*(n+1)
            for i in range(1,n+1):
                psum[i] = psum[i-1]+nums[i-1]
            
            msp = [0]*(n+1)
            prev = -10**10
            for i in range(n,0,-1):
                prev = max(prev,psum[i])
                msp[i] = prev

            for i in range(1,n-1):
                if(psum[i]>=0 and msp[i+1]>=psum[i]):
                    return True
            
            return False
        
        ok = False
        if(check(nums) or check(nums[::-1])):ok = True
        if(ok):return yes
        
        l = n-1
        curr = 0
        for i in range(n):
            curr+=nums[i]
            if(curr>=0):
                l = i
                break
        
        
        r = curr = 0
        for i in range(n-1,-1,-1):
            curr+=nums[i]
            if(curr>=0):
                r = i
                break
        
        if(l+1<=r-1):return yes
        return no
                
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)