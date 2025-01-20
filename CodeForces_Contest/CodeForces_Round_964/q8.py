from typing import List,Optional
from collections import deque
import sys
from math import ceil, floor, gcd, sqrt, log

def nCr(n,r):
    if(n<r or n<0 or r<0):return 0
    return fac[n]*pow(fac[r],mod-2,mod)*pow(fac[n-r],mod-2,mod)

class Solution:
    def run(self):
        low,high = 1,999
        while low<high:
            a = (2*low+high)//3
            b = (low+2*high)//3
            print("?",a,b,flush=True)
            ans = int(input().strip())
            if(ans==a*b):
                low=b+1
            elif(ans==a*(b+1)):
                low = a+1
                high = b
            elif(ans==((a+1)*(b+1))):
                high = a
        
        print("!",low,flush=True)
            
if __name__ == "__main__":
    # N = 2*(10**5)+5
    # mod = 10**9+7
    # fac = [1]*N
    # for i in range(1,N):
    #     fac[i] = (fac[i-1]*i)%mod
    for _ in range(int(input().strip())):
        Solution().run()