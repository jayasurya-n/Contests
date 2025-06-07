from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect, random
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

def ask(i):
    print(f"? {i+1}")
    sys.stdout.flush()
    return ii()

def sol(a,b):
    print(f"! {a} {b}")
    sys.stdout.flush()

def wa_sol():
    print(f"! -1")
    sys.stdout.flush()


class Solution:
    def run(self):
        n,k = lii()
        if(n==2*k):
            sol(k,k)
            return

        a = []
        for i in range(k):
            a.append(ask(i))
        
        b = [-1]*k
        for i in range(n-k,n):
            b[i%k] = ask(i)
        
        diff = -1
        for i in range(k):
            if(a[i]!=b[i]):
                diff = i
                break

        if(diff==-1):
            wa_sol()
            return

        low,high = 0,(n-1-diff)//k
        while low<=high:
            mid = (low+high)>>1
            pos = mid*k+diff
            if(pos>=n):
                high = mid-1
                continue
            if(ask(pos)==a[diff]):low = mid+1
            else:high = mid-1
        
        start = high*k+diff
        boundary = start
        crossed = False
        for i in range(start+1, min(n, start+k+1)):
            val = ask(i)
            if val == a[i%k]:boundary = i
            elif val == b[i%k]:
                crossed = True
                break
            else:
                wa_sol()
                return

        if not crossed:
            wa_sol()
            return

        alen = boundary + 1
        blen = n-alen
        if alen < k or blen < k:
            wa_sol()
            return
        sol(alen, blen)


if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()