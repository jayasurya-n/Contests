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
        n,r,c = lii()
        s = si()
        
        ans = []
        hash = set([(0,0)])
        x = y = 0
        for i in range(n):
            if(s[i]=='N'):x-=1
            elif(s[i]=='S'):x+=1
            elif(s[i]=='E'):y+=1
            elif(s[i]=='W'):y-=1
            
            if((x-r,y-c) in hash):ans.append('1')
            else:ans.append('0')
            hash.add((x,y))

        return "".join(ans)

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    seed = random.randint(0,10**9+7)
    for _ in range(1):
        ans = Solution().run()
        print(ans)