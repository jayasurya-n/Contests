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
        arr = lii()

        ans = 0
        for i in range(n):
            for j in range(i,n):
                ok = True
                prev = -1
                for k in range(i,j+1):
                    if(arr[k]>=2*(prev+1)+1):prev+=1
                    elif(arr[k]>=prev+1):prev = arr[k]
                    else:
                        ok = False
                        break
                if(ok):ans+=1
        return ans    

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)