from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

def nCr(n,r):
    if(n<r or n<0 or r<0):return 0
    return fac[n]*pow(fac[r],mod-2,mod)*pow(fac[n-r],mod-2,mod)

def prefixSum1D(arr,n):
    prefix = [0]*n
    prefix[0] = arr[0]
    for i in range(1,n):prefix[i] = prefix[i-1]+arr[i]
    return prefix

def prefixSum2D(arr,m,n):
    prefix = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            prefix[i][j] = arr[i][j]
            if i>0:prefix[i][j] += prefix[i-1][j]
            if j>0:prefix[a][b] += prefix[i][j-1]
            if i>0 and j>0:prefix[i][j] -= p[i-1][j-1]
    return prefix

class Solution:
    def run(self):
        k,l1,r1,l2,r2 = list(map(int,input().strip().split()))
        ans,n = 0,0
        while(True):
            div = k**n
            l3,r3 = ceil(l2/div),floor(r2/div)
            if(l3>r3):break
            cnt = max(0,min(r3,r1)-max(l3,l1)+1)
            ans+=cnt
            n+=1
        return ans

if __name__ == "__main__":
    # N = 2*(10**5)+5
    # mod = 10**9+7
    # fac = [1]*N
    # for i in range(1,N):
    #     fac[i] = (fac[i-1]*i)%mod
    yes = "YES"
    no = "NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)