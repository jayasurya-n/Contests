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
        A = lii()

        indices = [[] for _ in range(k+1)]
        for i in range(n):
            indices[A[i]].append(i)

        for i in range(1,k+1):
            indices[i] = sorted(indices[i])

        dp = [n**2]*n
        for id in indices[k]:dp[id] = 0
        # dp[i]: min cost reach from i to k
        # transition: 
        # for ind in indices[i]:
        #   dp[i] = dp[i+1]+min(ind-left,right-ind)
        # base: dp[k] = 0
        
        def bsIndex(nums,target):
            # works like bisect.left
            # if target is lesser than smallest then index=0
            # if target is larger than largest  then index=n
            low,high = 0,len(nums)-1
            while(low<=high):
                mid = (low+high)>>1
                if(nums[mid]>=target):high = mid-1
                else:low = mid+1
            return low

        for num in range(k-1,0,-1):
            for i in indices[num]:
                bs_ind = bsIndex(indices[num+1],i)
                
                if(bs_ind<len(indices[num+1])):
                    j = indices[num+1][bs_ind]
                    dp[i] = min(dp[i],dp[j]+j-i)
                
                if(bs_ind>0):
                    j = indices[num+1][bs_ind-1]
                    dp[i] = min(dp[i],dp[j]+i-j)
        
        ans = []
        for start in range(n):       
            curr = n**2
            bs_ind = bsIndex(indices[1],start)
            
            if(bs_ind<len(indices[1])):
                j = indices[1][bs_ind]
                curr = min(curr,dp[j]+j-start)
            
            if(bs_ind>0):
                j = indices[1][bs_ind-1]
                curr = min(curr,dp[j]+start-j)

            ans.append(curr)
        
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(*ans)