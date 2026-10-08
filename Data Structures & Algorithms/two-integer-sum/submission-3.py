class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps={}
        for i in range(0,len(nums)):
            find = target - nums[i]
            if find in maps:
                return [maps[find], i]
            maps[nums[i]]=i
        return 

            
            



        