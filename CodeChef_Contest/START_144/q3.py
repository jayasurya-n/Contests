from typing import List,Optional
import sys
class Solution:
    def run(self) -> Optional[list]:
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))

        freq = dict()
        for i in range(len(arr)):
            freq[arr[i]] = freq.get(arr[i],0)+1
        
        freqList = list(sorted(freq.items(),key=lambda x:-x[1]))
        prefixSum = [0]*len(freqList)

        prefixSum[0] = freqList[0][1]
        for i in range(1,len(freqList)):
            prefixSum[i] = prefixSum[i-1]+freqList[i][1]

        ans = 0
        for distinct in range(1,len(freqList)+1):
            mul = 1
            maxEle = prefixSum[distinct-1]
            while(mul*distinct<=n):
                if(maxEle>=mul*distinct):
                    ans = max(ans,mul*distinct)
                mul+=1
        return ans
                

# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        print(Solution().run())