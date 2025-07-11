from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

def kmp_search(text,pattern):
    if not pattern:
        return list(range(len(text) + 1))

    lps = [0]*len(pattern)
    length = 0 
    i = 1
    while i<len(pattern):
        if pattern[i]==pattern[length]:
            length+=1
            lps[i]=length
            i += 1
        else:
            if length!= 0:length=lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    result_indices = []
    i = j = 0
    while i<len(text):
        if text[i]==pattern[j]:
            i+=1
            j+=1

        if j==len(pattern):
            result_indices.append(i - j)
            j = lps[j - 1]
        elif i<len(text) and text[i]!=pattern[j]:
            if j!=0:j = lps[j - 1]
            else:i+=1

    return result_indices

class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        a,b,c = p.split('*')
        l1,l2,l3 = len(a),len(b),len(c)
        
        prefix = kmp_search(s,a)
        middle = kmp_search(s,b)
        suffix = kmp_search(s,c)

        # n = len(s)
        # ans = n+1
        # for i1 in prefix:
        #     i2 = bisect.bisect_left(middle,i1+l1)
        #     if(i2>=len(middle)):continue
        #     i3 = bisect.bisect_left(suffix,middle[i2]+l2)
        #     if(i3>=len(suffix)):continue
        #     ans = min(ans,suffix[i3]+l3-i1)

        # return ans if ans<n+1 else -1

        n = len(s)
        ans = n+1

        i = j = k = 0
        while i<len(prefix):
            while(j<len(middle) and middle[j]<prefix[i]+l1):j+=1
            if(j==len(middle)):break

            while(k<len(suffix) and suffix[k]<middle[j]+l2):k+=1
            if(k==len(suffix)):break

            ans = min(ans,suffix[k]-prefix[i]+l3)
            i+=1
            
        return ans if ans<n+1 else -1

# time complexity: O(n+m+n(logn)^2),O(n+m)
# space complexity: O(m+n),O(m+n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))