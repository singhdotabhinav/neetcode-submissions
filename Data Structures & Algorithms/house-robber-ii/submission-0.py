class Solution:
    def linear_rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        rob_list = [0] * len(nums)
        rob_list[0] = nums[0]
        rob_list[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            rob_list[i] = max(rob_list[i-2] + nums[i], rob_list[i-1])
        return rob_list[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        rob_list_1 = nums[:-1]
        linear_rob_0_n_minus_1 = self.linear_rob(rob_list_1)
        rob_list_2 = nums[1:]
        linear_rob_1_n = self.linear_rob(rob_list_2)
        return max(linear_rob_0_n_minus_1, linear_rob_1_n)