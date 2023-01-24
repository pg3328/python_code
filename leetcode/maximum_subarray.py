class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        opt=[]
        opt.append(nums[0])
        maximum = float("-inf")
        for i in range(1,len(nums)):
            opt.append(max(opt[i-1]+nums[i], nums[i]))
            if maximum < opt[len(opt)-1]:
                maximum = opt[len(opt)-1]
        return maximum

