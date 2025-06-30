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
        n = ii()
        arr = lii()
        arr.sort()

        # gmax = max(arr)
        # ans = 0
        # for i in range(n-2):
        #     for j in range(i+1,n-1):
        #         lower = gmax-arr[i]-arr[j]
        #         higher = arr[i]+arr[j]
        #         ind1 = bisect.bisect_right(arr,lower,j+1,n-1)
        #         ind2 = bisect.bisect_left(arr,higher,j+1,n-1)-1
        #         ans+=max(0,ind2-ind1+1)
        #         if(arr[i]+arr[j]>gmax):ans+=1
        # return ans

        gmax = arr[n-1]
        ans = 0
        for k in range(2,n):
            target = arr[k]
            if(k!=n-1):target = max(target,gmax-arr[k])
            i,j = 0,k-1
            while i<=j:
                if(arr[i]+arr[j]>target):
                    ans+=j-i
                    j-=1
                else:i+=1
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)