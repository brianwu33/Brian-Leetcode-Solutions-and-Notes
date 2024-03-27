class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i in range(len(nums)):
            num = nums[i]
            value = target - num
            if value in seen:
                return [seen.get(value), i]
            seen[num] = i
                