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
        
        maxi = max(arr)
        cnt = arr.count(maxi)
        if(n-cnt==0):
            print(no)
            return
        
        ans = []
        for i in range(n):
            if(arr[i]==maxi):ans.append(1)
            else:ans.append(2)
        print(yes)
        print(*ans)
            

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()