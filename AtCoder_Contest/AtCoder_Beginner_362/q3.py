from typing import List,Optional
import sys
class Solution:
    def run(self) -> Optional[list]:
        n = int(input().strip())
        arr = []
        for i in range(n):
            arr.append(list(map(int,input().strip().split())))
        
        lowest = sum([arr[i][0] for i in range(len(arr))])
        highest = sum([arr[i][1] for i in range(len(arr))])
        if(0<lowest or highest<0):
            print("No")
            return
        
        ans = [arr[i][0] for i in range(len(arr))]

        for i in range(len(ans)):
            if(lowest==0):break
            if(lowest+(arr[i][1]-arr[i][0])<=0):
                ans[i] = arr[i][1]
                lowest+=arr[i][1]-arr[i][0]
            else:
                ans[i] = arr[i][0]+abs(lowest)
                lowest=0            
        
        print("Yes")
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()





# time complexity: O(N)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(1):
        Solution().run()