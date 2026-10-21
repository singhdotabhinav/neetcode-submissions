class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = len(height) * [0]
        right_max = len(height) * [0]
        left_max[0] = height[0]
        trapped=0
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i])
        n = len(height)
        r=n-2
        right_max[n-1]=height[n-1]
        while(r>=0):
            right_max[r] = max(height[r], right_max[r + 1])
            r-=1

        for i in range(len(height)-1):
            trapped += min(left_max[i], right_max[i]) - height[i]
        return trapped 
                


        