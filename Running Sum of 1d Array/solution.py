def runningSum(self, nums: List[int]) -> List[int]:
      for i in range(1, len(nums)):
           nums[i] += nums[i - 1]
       return nums
 #nums is the given list
