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
        
        matched = []
        for i in range(n):
            if(arr[i]==i+1):matched.append(i+1)
        
        if(not matched):return 0
        m = len(matched)
        ans = (m+1)//2
        
        if(n%2==1 and m%2==1 and matched[m//2]==(n+1)//2):
            for i in range(m//2):
                x,y = matched[i]-1,matched[m-i-1]-1
                arr[x],arr[y] = arr[y],arr[x]
            
            ok = True
            half = (n+1)//2
            for i in range(half):
                if(arr[i]<half):
                    ok = False
                    break

            for i in range(half+1,n):
                if(arr[i]>half):
                    ok = False
                    break
            
            if(ok):ans = m//2
        
        return ans
            
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)