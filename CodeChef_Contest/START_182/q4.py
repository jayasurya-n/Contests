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
        
        def solve(s):
            b = []
            g = []
            end = None
            cnt = 1
            for i in range(n-1):
                if(s[i]==s[i+1]):cnt+=1
                else:
                    if(s[i]=='B' and cnt>=k):
                        b.append(cnt)
                        end = i
                        
                    elif(s[i]=='G' and cnt>=k):
                        g.append(cnt)
                        end = i
                    cnt = 1
            
            if(s[-1]=='B' and cnt>=k):
                b.append(cnt)
                end = n-1
            elif(s[-1]=='G' and cnt>=k):
                g.append(cnt)
                end = n-1
            
            if(not b and not g):return yes
            if(len(b)>=2 or len(g)>=2 or 
            (b and max(b)>=2*k-1) or 
            (g and max(g)>=2*k-1)):return no
            if(len(b)==1 and len(g)==1):return yes
            
            
            length = b[0] if b else g[0]
            start = end-length+1
            
            prefix = [0]*(n+1)
            cnt = 0
            for i in range(n-1,-1,-1):
                if(s[i]==s[start]):cnt+=1
                else:cnt = 0
                prefix[i] = cnt

            suffix = [0]*n
            cnt = 0
            for i in range(n):
                if(s[i]==s[start]):cnt+=1
                else:cnt = 0
                suffix[i] = cnt
                
            
            for i in range(n):
                if(start<=i<=end):continue
                upper = k-suffix[i]-1
                lower = prefix[i+1]+length-k+1
                if(upper>=lower):return yes
            
            return no
        
        if(solve(s)==yes or solve(s[::-1])==yes):return yes
        return no

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)