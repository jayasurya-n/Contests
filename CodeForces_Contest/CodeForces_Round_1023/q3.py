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
        n,k = lii()
        s = si()
        arr = lii()

        inf = -10**14

        pos = -1
        for i in range(n):
            if(s[i]=='0'):
                arr[i] = inf
                pos = i
        
        max_sum = curr = 0
        for i in range(n):
            if(curr<0):curr = 0
            curr+=arr[i]
            max_sum = max(max_sum,curr)

        if(max_sum>k):
            print("No")
            return
        if(pos==-1):
            if(max_sum==k):
                print("Yes")
                print(*arr)
            else:print("No")
            return 

        max_sum = curr = 0
        for i in range(pos+1,n):
            curr+=arr[i]
            max_sum = max(max_sum,curr)
        l = max_sum

        max_sum = curr = 0
        for i in range(pos-1,-1,-1):
            curr+=arr[i]
            max_sum = max(max_sum,curr)
        r = max_sum

        arr[pos] = k-l-r
        print("Yes")
        print(*arr)

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()