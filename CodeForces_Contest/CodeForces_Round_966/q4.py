from typing import List,Optional
from collections import deque
import sys, heapq
from math import ceil, floor, gcd, sqrt, log

def nCr(n,r):
    if(n<r or n<0 or r<0):return 0
    return fac[n]*pow(fac[r],mod-2,mod)*pow(fac[n-r],mod-2,mod)

class Solution:
    def run(self):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        s = input().strip()
        
        i,j = 0,n-1
        
        pairs = []
        while(i<j):
            while(i<n and s[i]=='R'):i+=1
            while(j>0 and s[j]=='L'):j-=1
            
            if(i<j):pairs.append((i,j))
            i+=1
            j-=1
        
        p = [0]*n
        p[0] = arr[0]
        for i in range(1,n):p[i] = p[i-1]+arr[i]
        
        ans = 0
        for k in range(len(pairs)):
            i,j = pairs[k]
            ans+=p[j]
            if(i>0):ans-=p[i-1]
        print(ans)
            


if __name__ == "__main__":
    # N = 2*(10**5)+5
    # mod = 10**9+7
    # fac = [1]*N
    # for i in range(1,N):
    #     fac[i] = (fac[i-1]*i)%mod
    for _ in range(int(input().strip())):
        Solution().run()