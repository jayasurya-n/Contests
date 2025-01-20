from typing import List,Optional
import sys
class Solution:
    def powerOfTwominusOne(x):
        return (x&(x+1))==0
    
    def solve(self,index,elements,arr,oR,dp):
        if(index==n):
            if(oR&(oR+1)==0):
                return elements
            else:return -sys.maxsize
        
        if(dp[index][oR]!=-1):return dp[index][oR]
        dp[index][oR] = max(self.solve(index+1,elements,arr,oR,dp),
                    self.solve(index+1,elements+1,arr,oR|arr[index],dp))
        return dp[index][oR]

    def func(self, arr:List,n:int) -> Optional[int]:
        maxORval = 0
        for i in range(len(arr)):
            maxORval |=arr[i]

        dp =  [[-1]*(maxORval+1) for _ in range(len(arr))]
        oR = 0
        return len(arr)-self.solve(0,0,arr,oR,dp)

    


# time complexity: O()
# space complexity: O()
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print("Answer",Solution().func(arr,n))