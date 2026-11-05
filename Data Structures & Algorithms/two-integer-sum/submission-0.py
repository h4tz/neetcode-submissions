class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set = {}

        for i, num in enumerate(nums):
            curr = num
            comp = target - curr
            if comp in set:
                return [set[comp], i]
            else:
                set[curr] = i

        