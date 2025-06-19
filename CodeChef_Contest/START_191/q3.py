from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect, random
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def run(self):
        n = ii()
        A = lii()
        B = lii()

        def check(x):
            need = have = 0
            for a,b in zip(A,B):
                if(a+b<=x):have+=(x-(a+b))//2
                else:need+=a+b-x
            return need<=have

        low,high = max(A),10**15
        while(low<=high):
            mid = (low+high)>>1
            if(check(mid)):high = mid-1
            else:low = mid+1
        return low
    

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)