class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n -1
        # def canwe(nums: List[int], mid:int, target: int) -> bool:
        #     if(nums[mid - 1] < target and nums[mid + 1] > target):
        #         return True
        #     return False

        if(nums[high] < target):
            return n

        while(low <= high):
            mid = low + (high - low) // 2
            if(nums[mid] < target):
                low = mid + 1
            else:
                high = mid - 1
        return low
