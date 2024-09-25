input = [2,2,1,1,1,2,2];

class Solution:
    def majorityElement(self, nums):
        holder = {}
        for number in nums:
            if number not in holder:
                holder[number] = 0
            else:
                holder[number] += 1
            # alternate solution:
            # have a count and element variable that we update
            # with the highest count and element with highest count
            # as we iterate through the list
            # if holder[number] >= count:
            #     count += 1
            #     element = number

        return max(holder, key=holder.get)

solution = Solution()
print(solution.majorityElement(input))