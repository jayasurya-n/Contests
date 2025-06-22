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
        n,x = lii()

        ans = [0]*(n+1)
        s = [i for i in range(1,n+1) if (i|x)==x]
        used = [False]*(n+1)


        for i in s:
            if(used[i] or i==x):continue
            j = x&(~i)
            if 1<=j<=n and (j|x) == x and not used[j]:
                ans[i], ans[j] = j, i
                used[i] = used[j] = True
        
        if 1 <=x<=n and not used[x]:
            for v in s:
                if v!=x and not used[v]:
                    ans[x], ans[v] = v,x
                    used[x] = used[v] = True
                    break

        rem = [i for i in range(1,n+1) if not used[i]]
        j = 0
        for i in range(1,n+1):
            if ans[i] == 0:
                ans[i] = rem[j]
                j += 1

        return ans[1:]

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(*ans)