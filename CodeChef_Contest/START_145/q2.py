from typing import List,Optional
from collections import deque
import sys
class Solution:
    def run(self):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        
        
        freq = dict()
        for i in range(len(arr)):
            freq[arr[i]] = freq.get(arr[i],0)+1
        
        if(len(freq)>2):return "NO"
        if(0 in freq or len(freq)==1):return "YES"
        else: return "NO"
        

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        print(Solution().run())