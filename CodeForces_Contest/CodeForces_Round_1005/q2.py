from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))
    
class Solution:
    def run(self):
        n = ii()
        nums = lii()

        hash = [0]*(n+1)
        for num in nums:hash[num]+=1
        
        ans = [-1,-1]
        max_cnt = 0
        
        i = 0
        while(i<n):
            if(hash[nums[i]]>1):
                i+=1
                continue
            
            cnt = 0
            start = i
            while(i<n and hash[nums[i]]==1):
                cnt+=1
                i+=1
            
            if(cnt>max_cnt):
                max_cnt = cnt
                ans = [start+1,start+cnt]
        
        if(max_cnt==0):return [0]
        return ans
        
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        for i in ans:
            print(i,end=" ")
        print()