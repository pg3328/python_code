class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output_sum = float("-inf")
        local_max = float("-inf")
        for i in range(0,len(nums)):
            local_max =nums[i]
            local_sum = local_max
            for j in range(i+1,len(nums)):
                local_sum = local_sum+nums[j]
                local_max = max(local_sum,local_max)
            output_sum = max(local_max,output_sum)
