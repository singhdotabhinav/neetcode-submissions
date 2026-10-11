class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, curr_sum = 0, 0
        res = len(nums)+1
        for r in range(len(nums)):
            curr_sum+=nums[r]
            while(curr_sum>=target):
                curr_sum -= nums[l]
                res = min(r-l+1, res)
                l+=1

        return 0 if res ==len(nums)+1 else res

            



        