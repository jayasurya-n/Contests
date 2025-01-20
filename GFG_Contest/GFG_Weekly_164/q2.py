from typing import List,Optional
import sys
class Solution:
    def removeOrder(self, n : int, arr : List[int], str : str) -> List[int]:
        arr.sort()
        i,j=0,n-1
        ans = []
        for k in range(n):
            if(str[k]=='0'):
                ans.append(arr[i])
                i+=1
            else:
                ans.append(arr[j])
                j-=1
        return ans



# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))