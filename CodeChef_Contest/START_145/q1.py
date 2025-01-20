from typing import List,Optional
from collections import deque
import sys
class Solution:
    def run(self):
        n,d = list(map(int,input().strip().split()))
        arr = list(map(int,input().strip().split()))

        close = True
        ans = 0
        for i in range(n):
            if(close):
                if(arr[i]>d):
                    close = False
                    ans+=1
            else:
                if(arr[i]<=d):
                    close = True
                    ans+=1
        return ans

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        print(Solution().run())