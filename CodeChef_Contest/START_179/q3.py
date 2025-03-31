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
        
        peaks = []
        for i in range(1,n-1):
            if((arr[i-1]>arr[i] and arr[i+1]>arr[i]) or 
               (arr[i-1]<arr[i] and arr[i+1]<arr[i])):peaks.append(i)
        
        kc2 = lambda x:(x*(x-1))//2
        
        if(not peaks):return kc2(n) 
        peaks = [0]+peaks+[n-1]
        ans = 0
        for i in range(1,len(peaks)-1):
            left = peaks[i]-peaks[i-1]+1
            right = peaks[i+1]-peaks[i]+1
            ans+=kc2(left)+kc2(right)+(left-1)*(right-1)
        
        for i in range(1,len(peaks)-2):
            right = peaks[i+1]-peaks[i]+1
            ans-=kc2(right)
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)