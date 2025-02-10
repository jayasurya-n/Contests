from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        n = int(input().strip())
        q = []
        for _ in range(n):
            q.append(list(map(int,input().strip().split())))
        
        arr = []
        for i in range(n):
            cnt = 0
            for j in range(n-1,-1,-1):
                if(q[i][j]==1):cnt+=1
                else:break
            arr.append(cnt)
        
        arr.sort()
        ans = 0
        for num in arr:
            if(num>=ans):ans+=1
        return min(ans,n)

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)