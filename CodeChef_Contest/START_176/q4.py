from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
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
        n = ii()
        a = si()
        b = si()
        
        ones = zeros = others = 0
        for i in range(n):
            if(a[i]==b[i]):
                if(a[i]=='1'):ones+=1
                else:zeros+=1
            else:others+=1
        
        # print(ones,zeros,others)
        ones%=2
        zeros%=2
        others%=2
        
        if((ones+zeros+others)<=1):return yes
        return no

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    yes,no = "YES","NO"
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)