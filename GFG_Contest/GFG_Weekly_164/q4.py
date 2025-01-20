from typing import List,Optional
import sys
class Solution:
    def sumofItems(self, n : int, prices : List[int], q : int, queries : List[List[int]]) -> List[int]:
        freq = dict()
        add = 0
        for i in prices:
            freq[i] = freq.get(i,0)+1
        
        totalSum = sum(prices) 
        ans = []
        for i in range(q):
            if(queries[i][0]==1):
                totalSum+=n*queries[i][1]
                add+=queries[i][1]
            else:
                x = queries[i][1]
                y = queries[i][2]

                totalSum-= freq.get(x-add,0)*x
                totalSum+= freq.get(x-add,0)*y

                freq[y-add] = freq.get(y-add,0) + freq.get(x-add,0)
                freq[x-add] = 0
            ans.append(totalSum)
        return ans







        return ans


# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(1):
        n = int(input().strip())
        prices = list(map(int,input().strip().split()))
        q = int(input().strip())
        queries = [list(map(int,input().strip().split())) for _ in range(q)]
        print(Solution().sumofItems(n,prices,q,queries))