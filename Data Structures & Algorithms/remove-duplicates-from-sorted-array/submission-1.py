class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:]= set(nums)
        nums[:] = sorted(nums)
        return len(nums)
        