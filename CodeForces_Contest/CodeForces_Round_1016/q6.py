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
        n,m = lii()
        a = lsi()
        b = []
        for _ in range(m):b.append(lsi())
        
        ans = 0
        for j in range(m):
            cnt = 0
            for i in range(n):
                if(b[j][i]==a[i]):cnt+=1
            ans = max(ans,cnt)

        for i in range(n):
            cnt = 0
            for j in range(m):
                if(b[j][i]==a[i]):cnt+=1
            if(cnt==0):return -1
        
        return 3*n-2*ans
        

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)