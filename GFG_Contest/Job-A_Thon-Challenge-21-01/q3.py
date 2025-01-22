from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def findKth(self, k : int, n : int) -> str:
        l=1
        while(True):
            curr = k**((l+1)//2)
            if(curr>=n):break
            n-=curr
            l+=1
        
        rev = []
        l_half = (l+1)//2
        n-=1
        
        for _ in range(l_half):
            rev.append(chr(ord('a')+n%k))
            n//=k    
        
        s = rev[::-1]
        if(l%2==1):s.pop()
        return "".join(s)+"".join(rev)

# time complexity: O(logn)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))