from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def findValidPair(self, s: str) -> str:
        hash = defaultdict(int)
        for ch in s:hash[ch]+=1
        
        valid = set()
        for ch,cnt in hash.items():
            if(cnt==int(ch)):valid.add(ch)
        
        for i in range(len(s)-1):
            if(s[i]==s[i+1]):continue
            if((s[i] in valid) and s[i+1] in valid):return s[i:i+2]
        return ""

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        s = input().strip()
        print(Solution().findValidPair(s))