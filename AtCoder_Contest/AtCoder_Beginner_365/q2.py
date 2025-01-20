from typing import List,Optional
from collections import deque
import sys
class Solution:
    def run(self):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        
        maxi = max(arr)
        
        if(arr[0]!=maxi):ans=0
        else:ans=1
        for i in range(len(arr)):
            if(arr[i]>arr[ans] and arr[i]<maxi):ans = i
        return ans+1


# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(1):
        print(Solution().run())