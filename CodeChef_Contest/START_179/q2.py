from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect, random
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

def factorial(n,mod):
    fac = [1]*n
    for i in range(1,n):
        fac[i] = (fac[i-1]*i)%mod
    return fac

def nCr(n,r,fac,mod):
    if(n<r or n<0 or r<0):return 0
    return fac[n]*pow(fac[r],mod-2,mod)*pow(fac[n-r],mod-2,mod)

class Solution:
    def run(self):
        n,k = lii()
        a = lii()
        b = lii()
        
        moves = 0
        gap = 10
        for i in range(n):
            x,y = a[i],b[i]
            if(y>=x):moves+=min(y-x,9-y+x)
            else:moves+=min(x-y,9-x+y)
            diff = abs(9-2*(abs(x-y)))
            gap = min(gap,diff)
        
        if(k<moves):return no
        if((k-moves)%2==0):return yes
        
        rem = k-moves
        if(gap<=rem):return yes
        return no
    
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    yes,no = "Yes","No"
    seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)