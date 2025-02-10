from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        n = int(input().strip())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        ha = defaultdict(int)
        hb = defaultdict(int)
        
        for num in a:ha[num]+=1
        for num in b:hb[num]+=1
        
        if(len(ha)==1):return yes if len(hb)>=3 else no
        if(len(hb)==1):return yes if len(ha)>=3 else no
        return yes
            
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)