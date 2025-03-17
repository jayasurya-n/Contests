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
        n = ii()
        arr = [1,2,3]
        
        while True:
            print(f"? {arr[0]} {arr[1]} {arr[2]}")
            sys.stdout.flush()
            inside = ii()
            
            if(inside==0):
                print(f"! {arr[0]} {arr[1]} {arr[2]}")
                sys.stdout.flush()
                break
            
            temp = []
            ok = False
            for k in range(3):
                print(f"? {arr[k%3]} {arr[(k+1)%3]} {inside}")
                sys.stdout.flush()
                new = ii()
                
                if(new==0):
                    print(f"! {arr[k%3]} {arr[(k+1)%3]} {inside}")
                    sys.stdout.flush()
                    ok = True
                    break
                
                temp.append(new)
                
            if(ok):break
            arr = temp
        

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(ii()):
        ans = Solution().run()