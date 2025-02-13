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
        
        hash = defaultdict(int)
        for num in nums:hash[num]+=1
        hash = sorted([[key,val] for key,val in hash.items()])
        
        all = True
        for i in range(len(hash)):
            if(hash[i][1]%2!=0):
                all = False
                break
        if(all):return yes
        
        for i in range(len(hash)-1):
            curr,cnt1 = hash[i]
            next,cnt2 = hash[i+1]
            diff = next-curr
            if(cnt1<2*diff+1):
                if(cnt1%2==1):return no
            else:hash[i+1][1]+=cnt1-2*diff
        
        # print("last:",hash[-1][1])
        return yes if hash[-1][1]%2==0 else no
        
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)