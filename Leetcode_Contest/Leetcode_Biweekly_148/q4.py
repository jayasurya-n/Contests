from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

def factorial(n,mod):
    fac = [1]*n
    for i in range(1,n):
        fac[i] = (fac[i-1]*i)%mod
    return fac

def nCr(n,r,fac,mod):
    if(n<r or n<0 or r<0):return 0
    return fac[n]*pow(fac[r],mod-2,mod)*pow(fac[n-r],mod-2,mod)


class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        # mod=10**9+7
        # fac = factorial(m*n+2,mod)
        # ways = nCr(m*n-2,k-2,fac,mod)
        
        # rowsum = 0
        # for d in range(0,m+1):
        #     rowsum = (rowsum+d*(m-d))%mod
        # rowsum = (rowsum*n*n)%mod
        
        # colsum = 0
        # for d in range(0,n+1):
        #     colsum = (colsum+d*(n-d))%mod
        # colsum = (colsum*m*m)%mod
        
        # ans = (((rowsum+colsum)%mod)*ways)%mod
        # return ans
        
        mod=10**9+7
        fac = factorial(m*n+2,mod)
        ways = nCr(m*n-2,k-2,fac,mod)
        
        rowsum = (m*(m-1)*(m+1)*n*n)%mod
        rowsum = (rowsum*pow(6,mod-2,mod))%mod
        
        colsum = (n*(n-1)*(n+1)*m*m)%mod
        colsum = (colsum*pow(6,mod-2,mod))%mod
        
        ans = (((rowsum+colsum)%mod)*ways)%mod
        return ans
        
# time complexity: O(m+n),O(1)
# space complexity: O(mn),O(mn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))