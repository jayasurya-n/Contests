from typing import List,Optional
import sys
class Solution:
    def func(self, C1,C2):
        if((max(C1[0],C2[0]) < min(C1[3],C2[3])) and 
            max(C1[1],C2[1]) < min(C1[4],C2[4]) and    
            max(C1[2],C2[2]) < min(C1[5],C2[5])):
            return "Yes"
        return "No"




# time complexity: O(1)
# space complexity: O(1)
t = int(input().strip())
if __name__ == "__main__":
    for i in range(t):
        C1 = list(map(int,input().strip().split()))
        C2 = list(map(int,input().strip().split()))
        print(Solution().func(C1,C2))