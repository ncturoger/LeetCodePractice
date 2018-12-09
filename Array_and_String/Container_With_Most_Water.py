class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        forward = 0
        back = len(height) - 1
        max_v = 0
        last_height = None
        while forward < back:
            max_v = max(max_v, abs(back - forward) * min(height[forward], height[back]))
            if height[forward] < height[back]:
                forward += 1
            
            else:
                back -= 1

        print(max_v)
        return max_v

assert Solution().maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert Solution().maxArea([2,3,4,5,18,17,6]) == 17