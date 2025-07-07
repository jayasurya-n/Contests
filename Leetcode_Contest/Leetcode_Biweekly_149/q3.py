from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        
        gaps = [(startTime[0],-1)]
        for i in range(n-1):gaps.append((startTime[i+1]-endTime[i],i))
        gaps.append((eventTime-endTime[-1],n-1))
        gaps.sort()
        max_freetime = gaps[-1][0]
        
        def bsIndex(nums,target):
            low,high = 0,len(nums)-1
            while(low<=high):
                mid = (low+high)//2
                if(nums[mid][0]>=target):high = mid-1
                else:low = mid+1
            return low
        
        for i in range(n):
            duration = endTime[i] - startTime[i]
            free_time = startTime[i+1] if i+1<n else eventTime
            free_time-= endTime[i-1] if i>0 else 0
            max_freetime = max(max_freetime,free_time-duration)
            
            ind = bsIndex(gaps,duration)
            while(ind<len(gaps) and (gaps[ind][1]==i or gaps[ind][1]==i-1)):ind+=1
            if(ind==len(gaps)):continue
            
            max_freetime = max(max_freetime,free_time)
        return max_freetime

# time complexity: O(nlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        eventTime = int(input().strip())        
        startTime = list(map(int,input().strip().split()))
        endTime = list(map(int,input().strip().split()))
        print(Solution().maxFreeTime(eventTime,startTime,endTime))