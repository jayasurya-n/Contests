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
        
        def check(mid,arr):
            # subsets must contain 0 to m-1
            cnt = 0
            hash = set()
            i = mex = 0
            while(i<n):
                hash.add(seed^arr[i])
                while(seed^mex in hash):mex+=1
                if(mex>=mid):
                    cnt+=1
                    hash = set()
                    mex = 0
                i+=1
            return True if cnt>=k else False
                
        low,high = 0,max(arr)+1
        while(low<=high):
            mid = (low+high)>>1
            if(check(mid,arr)):low = mid+1
            else:high = mid-1
        return high
        
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)