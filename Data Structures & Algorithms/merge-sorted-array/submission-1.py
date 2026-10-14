class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        final_list = []
        for each in range(0, m):
            final_list.append(nums1[each])
        for each in range(0, n):
            final_list.append(nums2[each])
        final_list.sort()
        nums1[:] = final_list
        
        