from typing import List,Optional
from collections import deque
import sys

def nCr(n,r):
    if(n<r or n<0 or r<0):return 0
    return fac[n]*pow(fac[r],mod-2,mod)*pow(fac[n-r],mod-2,mod)

class Solution:
    def run(self):
        n,k = list(map(int,input().strip().split()))
        arr = list(map(int,input().strip().split()))

        c0,c1 = 0,0
        for i in range(n):
            if(arr[i]==1):c1+=1
            else:c0+=1
        
        ans = 0
        for ones in range(k//2+1,c1+1):
            ans=(ans+(nCr(c1,ones)*nCr(c0,k-ones))%mod)%mod
        return ans
        
            
# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    N = 2*(10**5)+5
    mod = 10**9+7
    fac = [1]*N
    for i in range(1,N):
        fac[i] = (fac[i-1]*i)%mod
    
    for _ in range(int(input().strip())):
        print(Solution().run())

