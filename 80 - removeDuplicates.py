class Solution:
    def removeDuplicates(self, nums) -> int:
        currentNum = 0
        count = 0
        i = 0
        while i < len(nums):
            if currentNum != nums[i]:
                currentNum = nums[i]
                count = 1
                i += 1
            else:
                count += 1
                i += 1
            if count > 2:
                del nums[i-1]
                i -= 1

        return nums

listInput = [0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3]
# listInput= [1,1,1,2,2,3]
# listInput= [1,1,1]
solution = Solution()
print(solution.removeDuplicates(listInput))