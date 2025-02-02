from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        n,m = list(map(int,input().strip().split()))
        s,t = [],[]
        for _ in range(n):s.append(input().strip())
        for _ in range(m):t.append(input().strip())
        
        for a in range(n-m+1):
            for b in range(n-m+1):
                bool = True
                for i in range(m):
                    for j in range(m):
                        if(s[i+a][j+b]!=t[i][j]):
                            bool = False
                            break
                    if(not bool):break
                if(bool):return [a+1,b+1]
                
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(1):
        ans = Solution().run()
        print(ans[0],ans[1])