from typing import List
class Solution:
    def ABA_BAB(self, s: str, n: int) -> int:
        hash_set = set()
        for i in range(0,len(s)-2):
            for j in range(i,len(s)-2):
                if(s[j:j+3]=='ABA'):pass

            


# time complexity: O(2*n) first case, O(n) in second case
# space complexity: O(1) in both cases as the dictionary takes only 3 elements at max 
if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    print(Solution().ABA_BAB(s,n))