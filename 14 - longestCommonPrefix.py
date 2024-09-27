class Solution:
    def longestCommonPrefix(self, strs) -> str:
        longest_common_prefix = strs[0]

        def find_longest(a, b):
            common_prefix = ""
            for a, b in zip(longest_common_prefix, word):
                if a == b:
                    common_prefix += a
                else:
                    break
            return common_prefix
        for word in strs:
            current = find_longest(longest_common_prefix, word)
            if len(current) < len(longest_common_prefix):
                longest_common_prefix = current

        return longest_common_prefix

        

s_input = ["flower","flow","flight"]
solution = Solution()
print(solution.longestCommonPrefix(s_input))