class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l =0
        r= len(heights)-1
        while(r>l):
            if heights[l]>heights[r]:
                area = min(heights[l],heights[r]) * abs(r-l)
                max_area = max(area, max_area)
                r-=1

            elif heights[l]<heights[r]:
                area = min(heights[l],heights[r]) * abs(r-l)
                max_area = max(area, max_area)
                l+=1
            else:
                area = min(heights[l],heights[r]) * abs(r-l)
                max_area = max(area, max_area)
                l+=1
                r-=1
        return max_area

        