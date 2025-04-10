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
        if(k<n//2):
            print(-1)
            return
        
        ch = ['A','B','C']
        s,t = [],[]
        curr = n
        for i in range(n):
            if(k==curr//2):
                for j in range(i,n):
                    if((i-j)%2==1):
                        s.append(ch[(i+2)%3])
                        t.append(ch[(i+2)%3])
                    else:
                        s.append(ch[(i+1)%3])
                        t.append(ch[i%3])
                break
            else:
                s.append(ch[i%3])
                t.append(ch[i%3])
                k-=1
                curr-=1
        
        print("".join(s))
        print("".join(t))
        

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()