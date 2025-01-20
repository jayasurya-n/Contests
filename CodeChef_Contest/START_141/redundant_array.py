from typing import List
import sys
class Solution:
    def redundantArray(self,arr,n):
        ans = n*1
        freq = dict()

        for i in range(n):
            freq[arr[i]] = freq.setdefault(arr[i],0)+1
        
        val,maxFreq = sys.maxsize,0 
        for key,value in freq.items():
            if(value>maxFreq):
                maxFreq = value
                val = key
            elif(value==maxFreq):
                val = min(val,key)

        freq_1 = freq.get(1,0)
        ans = min(ans,(n-maxFreq)*val,n-freq_1)
        return ans


            
# time complexity: 
# space complexity: 
if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().redundantArray(arr,n))