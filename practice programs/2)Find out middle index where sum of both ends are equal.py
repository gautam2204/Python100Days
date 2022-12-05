'''Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].'''


class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        for index,value in enumerate(nums):
            rem=target-value
            if rem in nums and  nums.index(rem) != index:
                return nums.index(rem),index

            # current_index = nums.index(current_num)
            # for nextNum in nums:
            #     if not nums.index(nextNum) == current_index:
            #         sumVal = sum([current_num,nextNum])
            #         if sumVal==target:
            #             return current_index,nums.index(nextNum)

sol = Solution()
print(sol.twoSum(nums=[2,7,11,15],target=9))




