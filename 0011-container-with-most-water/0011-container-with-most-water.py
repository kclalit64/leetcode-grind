class Solution:
    def maxArea(self, height: List[int]) -> int:

        #BRUTEFORCE APPROACH
        # maxVol = 0
        # for a in range(len(height)):
        #     for b in range(a+1, len(height)):
        #         vol = min(height[a],height[b])*(b-a)
        #         if vol > maxVol:
        #             maxVol = vol
        # return maxVol

        #TWO POINTER APPROACH O(N)
        l, r = 0, len(height)-1
        maxVol = 0
        while 1<=r:
            vol = min(height[l], height[r])*(r-l)
            maxVol = max(maxVol, vol)
            if height[l]<height[r]:
                l = l + 1
            else:
                r = r - 1
        return maxVol
