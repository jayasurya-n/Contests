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
        a = lii()
        b = lii()

        self.ans = []
        def sort(a,type):
            for i in range(n-1):
                for j in range(n-1):
                    if(a[j]>a[j+1]):
                        a[j],a[j+1] = a[j+1],a[j]
                        self.ans.append([type,j+1])
                
        sort(a,1)
        sort(b,2)

        for i in range(n):
            if(a[i]>b[i]):
                self.ans.append([3,i+1])
        
        print(len(self.ans))
        for x in self.ans:
            print(*x)

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()