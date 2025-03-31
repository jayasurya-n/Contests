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
        n = ii()
        arr = lii()
        
        if(n>=32):return '0'*n
        
        def check(arr):
            n = len(arr)
            if(n==1):return True
            diff = []
            for i in range(n-1):
                ele = arr[i+1]-arr[i]
                if(ele<=0):return False
                diff.append(ele)
            return check(diff)
        
        ans = []
        for i in range(n):
            new = arr[:i]+arr[i+1:]
            ans.append('1' if check(new) else '0')
        return "".join(ans)

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)