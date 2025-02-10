from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect, functools
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        n = int(input().strip())
        adj = []
        for _ in range(n):adj.append(input().strip())
        
        def compare(x,y):
            if(x==y):return 0
            if(x<y):
                if(adj[x-1][y-1]=='1'):return -1
                return 1
            else:
                if(adj[x-1][y-1]=='1'):return 1
                return -1
        
        ans = list(range(1,n+1))
        ans.sort(key=functools.cmp_to_key(compare))
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        for num in ans:
            print(num,end =" ")
        print()
