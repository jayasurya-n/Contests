from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        n,m,k = list(map(int,input().strip().split()))
        if((n<k and m<k) or abs(m-n)>k):return -1
        
        ans = []
        s = ['0','1'] if n>=m else ['1','0']
        if(m>n):n,m = m,n
        
        ans = [s[0]]*k
        ans.extend([s[1]+s[0]]*(n-k)) 
        ans.extend([s[1]]*(m-n+k))
        return "".join(ans)
        
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)