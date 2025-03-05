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
        n,l,r = lii()
        arr = lii()
        
        pxor = [0]*n
        pxor[0] = arr[0]
        for i in range(1,n):
            pxor[i] = arr[i]^pxor[i-1]
        
        if(n%2==0):
            last = pxor[(n//2)-1]
            arr.append(last)
            pxor.append(last^pxor[n-1])
            n+=1
            
            
        # def rec(m):
        #     # print("m",m)
        #     if(m<=n):return arr[m-1]
        #     elif(n<m<=2*n):return pxor[(m//2)-1]
            
        #     k = m//2
        #     if(k%2==1):return pxor[n-1]
        #     else:return pxor[n-1]^rec(k)
        
        m = l
        ans = 0
        while True:
            if(m<=n):
                ans^=arr[m-1]
                break
            elif(n<m<=2*n):
                ans^=pxor[(m//2)-1]
                break
            
            k = m//2
            if(k%2==1):
                ans^=pxor[n-1]
                break
            else:
                ans^=pxor[n-1]
                m//=2    
            
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)