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
        
        s = list(s)
        for i,ch in enumerate(s):
            if(s[i]=='o'):
                if(i-1>=0):s[i-1]='.'
                if(i+1<n):s[i+1]='.'
        
        rem = k - s.count('o')
        if rem == 0:
            return "".join(ch if ch != '?' else '.' for ch in s)
        
        maxi = cnt = 0
        counts = []
        for i in range(n):
            if(s[i]=='?'):cnt+=1
            else:
                if(cnt>0):counts.append(cnt)
                maxi+=(cnt+1)//2
                cnt = 0
        if(cnt>0):counts.append(cnt)
        maxi+=(cnt+1)//2
        
        if(rem<maxi):return "".join(s)
        
        i = j = 0
        while(i<n):
            if s[i] == '?':
                if(counts[j]%2==0):
                    while(i<n and s[i]=='?'):i+=1
                else:
                    cnt = 0
                    while(i<n and s[i]=='?'):
                        s[i] = 'o' if cnt%2==0 else '.'
                        cnt+=1
                        i+=1
                j+=1
            else:i+=1
        return "".join(s) 
        
if __name__ == "__main__":
    
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)