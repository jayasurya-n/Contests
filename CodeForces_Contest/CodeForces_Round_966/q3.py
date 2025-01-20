from typing import List,Optional
from collections import deque
import sys, heapq
from math import ceil, floor, gcd, sqrt, log

def nCr(n,r):
    if(n<r or n<0 or r<0):return 0
    return fac[n]*pow(fac[r],mod-2,mod)*pow(fac[n-r],mod-2,mod)

class Solution:
    def run(self):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        m = int(input().strip())
        strings = [input().strip() for _ in range(m)]
        
        def check(s):
            if(len(s)!=n):return no
            map1 = dict()
            map2 = [-1]*26
            
            for i in range(n):
                if(arr[i] in map1 and map1[arr[i]]!=s[i]):return no
                if(map2[ord(s[i])-97]!=-1 and map2[ord(s[i])-97]!=arr[i]):return no
                map1[arr[i]]=s[i]
                map2[ord(s[i])-97] = arr[i]
            return yes
        
        ans = [False]*m     
        for i in range(m):ans[i] = check(strings[i])
        return ans
        
        
if __name__ == "__main__":
    # N = 2*(10**5)+5
    # mod = 10**9+7
    # fac = [1]*N
    # for i in range(1,N):
    #     fac[i] = (fac[i-1]*i)%mod
    yes = "YES"
    no = "NO"
    for _ in range(int(input().strip())):
        ans = Solution().run()
        for i in range(len(ans)):
            print(ans[i])