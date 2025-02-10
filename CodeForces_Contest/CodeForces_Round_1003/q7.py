from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        adj = [[] for _ in range(n)]
        
        ans = ['0']*n
        for _ in range(n-1):
            u,v = list(map(int,input().strip().split()))
            if(arr[u-1]==arr[v-1]):ans[arr[u-1]-1] = '1'
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        
        for u in range(n):
            values = []
            for v in adj[u]:values.append(arr[v])
            values.sort()
            for j in range(len(values)-1):
                if(values[j]==values[j+1]):ans[values[j]-1]='1'
        
        return "".join(ans)

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)