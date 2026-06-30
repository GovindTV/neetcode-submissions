class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = {}
        for i in range(len(nums)):
            if target - nums[i] in ind:
                return [ind[target - nums[i]], i]

            if nums[i] not in ind:
                ind[nums[i]] = i
            
