from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        n,p = list(map(int,input().strip().split()))
        heights = list(map(int,input().strip().split()))
        time = [-1]*n
        
        pq = []
        for i,h in enumerate(heights):
            if(h==0):
                time[i] = 0
                pq.append((0,i))
        
        while pq:
            t,i = heapq.heappop(pq)
            for di in [1,-1]:
                if(0<=i+di<n and time[i+di]==-1):
                    time[i+di] = max(t,ceil(heights[i+di]/p))
                    heapq.heappush(pq,(time[i+di],i+di))
        return time
    
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        for num in ans:
            print(num,end= " ")
        print()