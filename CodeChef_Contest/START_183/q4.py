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
        n,m = lii()
        total = n*(n-1)//2
        zeros = total-m
        
        required = n-1
        mini = None
        if(required<=zeros):mini = 0
        else:mini = required-zeros
        
        # c = n*n-n-2*m
        # k = ceil((sqrt(1+4*c)+1)/2)
        # maxi = min(n-k,m)
        
        low,high = 1,n
        while(low<=high):
            mid = (low+high)>>1
            val = (n*(n-1))//2 - (mid*(mid-1))//2
            if(val<=m):high = mid-1
            else:low = mid+1
        
        maxi = min(n-low,m)
        ans = (maxi*(maxi+1))//2 - ((mini-1)*(mini))//2
        return ans 
        
        
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)