from typing import List,Optional
import sys
class Solution:
    def func(self, arr:List,k,x,n) -> Optional[int]:
        for i in range(n):
            print(arr[i],end=" ")
            if(i+1==k):
                print(x,end=" ")
        print()


# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    n,k,x = list(map(int,input().strip().split()))
    arr = list(map(int,input().strip().split()))
    Solution().func(arr,k,x,n)