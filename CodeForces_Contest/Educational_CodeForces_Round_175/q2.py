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
        n,x,k = lii()
        s = si()
        
        zero = None
        curr = 0
        for i,ch in enumerate(s):
            if(ch=='L'):curr+=1
            else:curr-=1
            if(curr==0):
                zero = i+1
                break

        ans = 0
        curr = 0
        for i,ch in enumerate(s):
            if(ch=='L'):curr+=1
            else:curr-=1
            if(curr==x):
                ans = 1
                break
        
        if(ans==0):return 0
        elif(not zero):return 1
        ans = 1+(k-(i+1))//(zero)
        return ans
        

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)