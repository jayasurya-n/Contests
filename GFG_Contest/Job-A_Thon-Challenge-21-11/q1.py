from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def maxDistance(self, s, x):
        indices = [i for i,ch in enumerate(s) if ch==x]
        if(len(indices)<=1):return -1
        
        count = set()
        for i in range(indices[0]+1,indices[-1]):
            if(s[i]!=' ' and s[i]!=x):count.add(s[i])
        return len(count)

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        s = input().strip()
        x = input().strip()
        print(Solution().maxDistance(s,x))