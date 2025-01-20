from typing import List,Optional
import sys
class Solution:
    def getSegments(self, arr, n, x):
        segments=1

        or_value = 0 
        for i in range(n):
            if(or_value|arr[i]>x):  
                segments+=1
                or_value=arr[i]
            else:or_value|=arr[i]
        return segments
        


# time complexity: O(n)
# space complexity: O(1)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        arr = list(map(int,input().strip().split()))
        x = int(input().strip())
        print(Solution().getSegments(arr,len(arr),x))