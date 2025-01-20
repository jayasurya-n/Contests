from typing import List,Optional
import sys
class Solution:
    def run(self) -> Optional[list]:
        n,m = list(map(int,input().strip().split()))
        matrix = [list(map(int,input().strip().split())) for _ in range(n)]

        if(n==1 and m==1):return -1
        if(n==1):
            matrix[0] = matrix[0][::-1]
            if(m%2==1):matrix[0][m//2], matrix[0][0] =  matrix[0][0], matrix[0][m//2]

        matrix = matrix[::-1]
        if(n%2==1):matrix[n//2],matrix[0] = matrix[0],matrix[n//2]
        return matrix
        



# time complexity: O(n*m)
# space complexity: O(n*m)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        matrix = Solution().run()
        if(matrix==-1):print("-1")
        else:
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    print(matrix[i][j],end = " ")
                print()