from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

def seive(n):
    lp = list(range(n+1))
    for i in range(2,int(n**0.5)+1):
        if(lp[i]==i):
            for j in range(i*i,n+1,i):
                if(lp[j]==j):lp[j] = i
    return lp


class Solution:
    def run(self):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        
        ones = primes = 0
        fpq = defaultdict(int)
        fps = defaultdict(int)
        fp = defaultdict(int)
        
        for ele in arr:
            if(ele==1):ones+=1
            elif(lp[ele]==ele):
                primes+=1
                fp[ele]+=1
            elif(lp[ele]**2==ele):fps[ele]+=1
            elif(lp[ele]*lp[ele//lp[ele]]==ele):fpq[ele]+=1
        
        ans = 0
        for ele,cnt in fps.items():
            ans+=cnt*ones
            ans+=cnt*fp[ele//lp[ele]]
            ans+=cnt*(cnt+1)//2
        
        for ele,cnt in fpq.items():
            ans+=cnt*ones
            ans+=cnt*(fp[lp[ele]]+fp[lp[ele//lp[ele]]])
            ans+=cnt*(cnt+1)//2
        
        for ele,cnt in fp.items():
            ans+=(cnt)*(primes-cnt)/2
        return int(ans)

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    lp = seive(n=2*(10**5))
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)