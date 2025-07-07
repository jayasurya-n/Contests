from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        
        max_freetime = max(startTime[0],eventTime-endTime[-1])
        for i in range(n-1):
            max_freetime = max(max_freetime,startTime[i+1]-endTime[i])
        
        times = [endTime[i]-startTime[i] for i in range(n)]
        for i in range(1,n):times[i]+=times[i-1]

        i=j=0
        while(j<n):
            while(j-i+1>k):i+=1
            free_time = startTime[j+1] if j+1<n else eventTime
            free_time-= endTime[i-1] if i>0 else 0
            free_time-=times[j]-(times[i-1] if i>0 else 0)
            max_freetime = max(max_freetime,free_time)            
            j+=1
        return max_freetime

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        eventTime = int(input().strip())        
        k = int(input().strip())
        startTime = list(map(int,input().strip().split()))
        endTime = list(map(int,input().strip().split()))
        print(Solution().maxFreeTime(eventTime,k,startTime,endTime))