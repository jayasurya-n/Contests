from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        n,w = list(map(int,input().strip().split()))
        queues = [deque() for _ in range(w)]
        for num in range(n):
            x,y = list(map(int,input().strip().split()))
            x-=1
            y-=1
            queues[x].append((y,num))
        
        blocks = [sys.maxsize]*n
        
        on = True
        while on:
            time = 0
            to_removed = []
            
            for j in range(w):
                if(not queues[j]):
                    on = False
                    break
                t,num = queues[j].popleft()
                time = max(time,t)
                to_removed.append(num)

            if(on):
                for num in to_removed:blocks[num] = time+1

        q = int(input().strip())
        for _ in range(q):
            query = list(map(int,input().strip().split()))
            t,num = query[0],query[1]-1
            
            if(t<blocks[num]):print(yes)
            else:print(no)
            
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    yes,no = "Yes","No"
    for _ in range(1):
        ans = Solution().run()