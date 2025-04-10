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
        
        if(n==1 and arr[0]==0):return [-1]
        if(n==1 and arr[0]!=0):return [arr[0],arr[0]]
        
        maxi = max(arr)
        mini = min(arr)
        if(maxi>0):return [maxi,maxi]
        if(mini<0):return [mini,mini]
        return [-1]
        

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(*ans)