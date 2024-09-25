class Solution:
    def twoSum(self, nums, target: int):
        num_holder = {}

        for i in range(len(nums)):
            partner = target - nums[i]
            if partner in num_holder:
                return [num_holder[partner], i]
            num_holder[nums[i]] = i

        return []

input_nums = [2,7,11,15]
input_target = 9
solution = Solution()
print(solution.twoSum(input_nums, input_target))