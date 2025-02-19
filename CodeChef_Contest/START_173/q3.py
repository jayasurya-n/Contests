from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def run(self):
        n,m = lii()
        a = lii()
        b = lii()
        
        if(len(b)==1):
            for i in range(n):
                if(a[i]>b[0]):a[i] = b[0]
            return a
        
        smallest = min(b)
        ind = b.index(smallest)
        greater = False
        
        for i in range(0,n-m+1):
            if(a[i]<smallest):continue

            if(a[i]==smallest):
                for j in range(m-1):
                    if(a[i+1+j]<b[(ind+1+j)%m]):break
                    elif(a[i+1+j]==b[(ind+1+j)%m]):continue
                    elif(a[i+1+j]>b[(ind+1+j)%m]):
                        greater = True
                        break
                    
            if(a[i]>smallest or greater):
                for j in range(i,n-m+1):
                    a[j] = smallest
                
                for j in range(m-1):
                    a[j+n-m+1] = b[(ind+1+j)%m]
                
                break

        return a
    
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        for num in ans:
            print(num,end=" ")
        print()