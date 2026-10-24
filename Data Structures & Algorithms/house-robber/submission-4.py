class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_list=[]
        for each in nums:
            rob_list.append(0)
        if len(nums)==0:
            return None
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            if nums[1]>nums[0]:
                return nums[1]
            else:
                return nums[0]
        rob_list[0]=nums[0]
        rob_list[1]=max(nums[1], nums[0])
        for i in range(2,len(nums)):
            rob_list[i]= max(rob_list[i-2] + nums[i], rob_list[i-1])
        max_val = rob_list[0]
        for num in rob_list[1:]:
            if num > max_val:
                max_val = num
        return max_val

        