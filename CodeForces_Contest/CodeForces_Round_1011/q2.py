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
        
        if(arr.count(0)==0):
            print(1)
            print(f"{1} {n}")

        elif(arr[0]!=0 and arr[n-1]!=0):
            print(2)
            print(f"{1} {n-1}")
            print(f"{1} {2}")
        
        elif(arr[0]==0 and arr[n-1]!=0):
            print(2)
            print(f"{1} {n-1}")
            print(f"{1} {2}")
        
        elif(arr[0]!=0 and arr[n-1]==0):
            print(2)
            print(f"{2} {n}")
            print(f"{1} {2}")
            
        else:
            if(arr[2:n-2].count(0)==0):
                print(3)
                print(f"{1} {2}")
                n-=1
                print(f"{n-1} {n}")
                n-=1
                print(f"{1} {n}")
            else:
                print(4)
                print(f"{1} {2}")
                n-=1
                print(f"{n-1} {n}")
                n-=1
                print(f"{1} {n-1}")
                print(f"{1} {2}")

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()