from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        n,m = list(map(int,input().strip().split()))
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))

        a[0] = min(a[0],b[0]-a[0])
        for i in range(1,n):
            mini = min(a[i],b[0]-a[i])
            maxi = max(a[i],b[0]-a[i])
            if(mini>=a[i-1]):a[i] = mini
            elif(maxi>=a[i-1]):a[i] = maxi
            else:return no 
        return yes
        
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)