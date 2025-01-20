from typing import List,Optional
import sys
class Solution:
    def func(self,n:int) -> Optional[int]:
        arr = [1]*(n+1)
        for k in range(2,n+1):
            for i in range(k,n+1,k):
                arr[i]=i
        return arr[1:]



# time complexity: O(n)
# space complexity: O(n)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        n = int(input().strip())
        arr = Solution().func(n)
        for i in range(len(arr)):
            print(arr[i],end = " ")
        print()