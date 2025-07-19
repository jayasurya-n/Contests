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
        
        arr.sort(reverse=True)
        psum = [0]*n
        for i in range(n):
            psum[i] = arr[i]+(psum[i-1] if i>0 else 0)

        def solve(i,k):
            ans = psum[i]
            length = i+1
            rem = k-length
            if(rem<=length):
                ans+=(rem)*(length-1)
                ans-=((rem)*(rem-1))//2
            return ans

        ans = []
        for k in range(1,2*n+1):
            low,high = 0,min(n-1,k-1)
            while(low<=high):
                mid = (low+high)>>1
                if(solve(mid,k)>=solve(max(mid-1,0),k)):low = mid+1
                else:high = mid-1
            ans.append(solve(high,k))
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(*ans)