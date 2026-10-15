class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_nums={}
        for each in nums:
            count_nums[each]=0
        for each in nums:
            count_nums[each]+=1
        print(count_nums)
        max_count = -1
        for key, value in count_nums.items():
            if value > max_count:
                max_count = value
                majority_element = key
        return majority_element
        
        