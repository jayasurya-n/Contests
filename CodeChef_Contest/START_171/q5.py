from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

class Solution:
    def run(self):
        n,k = list(map(int,input().strip().split()))
        arr = list(map(int,input().strip().split()))
        mod = 10**9+7
        zeros = arr.count(0)
        
        ans = pow(k,zeros,mod)
        
        c=0
        for i in range(0,n//2):
            if(arr[i]+arr[n-1-i]==0):c+=1
            elif(arr[i]!=0 and arr[n-1-i]!=0 
                 and arr[i]!=arr[n-1-i]):return ans
        
        rev_pairs = pow(k,2*c,mod)
        palindromes = pow(k,c,mod)
        if(n&1 and arr[n//2]==0):
            rev_pairs = (rev_pairs*k)%mod
            palindromes = (palindromes*k)%mod
        
        extra = (rev_pairs-palindromes+mod)%mod
        extra = extra*pow(2,mod-2,mod) #extra/2
        return (ans-extra+mod)%mod

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        print(ans)