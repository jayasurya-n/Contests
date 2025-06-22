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
        s = si()
        mod = 998244353

        indices = []
        for i in range(n-3):
            if(s[i]==s[i+1]):continue
            if(s[i]==s[i+2] and s[i+1]==s[i+3]):
                indices.append(i)
        
        ans = 0
        curr = 1
        count = [1]*len(indices)
        for j in range(1,len(indices)):
            incr = curr
            if(j-1>=0 and indices[j-1]==indices[j]-1):
                incr=(incr-count[j-1]+mod)%mod
            
            if(j-2>=0 and indices[j-2]==indices[j]-2):
                incr=(incr-count[j-2]+mod)%mod
            
            count[j]=(count[j]+incr)%mod
            curr=(curr+count[j])%mod
        
        # print("count",count)
        return (sum(count)+1)%mod



if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)