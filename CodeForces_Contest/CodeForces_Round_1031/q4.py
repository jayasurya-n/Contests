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
        a = lii()
        b = lii()

        def solve(a,b):
            score = 0
            i = j = 0
            for _ in range(n):
                if(a[i]>b[j]):
                    score+=1
                    i+=1
                else:j+=1
            return score

        actual_score = solve(a,b)

        def check(k):
            score = actual_score
            if(k==0 or k ==n):return score>=k
            
            i1 = a.index(min(a[:k]))
            i2 = a.index(max(a[k:]))

            if(a[i1]>a[i2]):return score>=k
            a[i1],a[i2] = a[i2],a[i1]
            score = max(score,solve(a,b))
            a[i1],a[i2] = a[i2],a[i1]
            return score>=k

        low,high = 0,n
        while(low<=high):
            mid = (low+high)>>1
            if(check(mid)):low = mid+1
            else:high = mid-1
        return high

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)