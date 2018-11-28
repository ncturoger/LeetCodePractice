class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_prefix = ""
        if strs:
            min_length = min([len(item) for item in strs])
            i = 0
            if min_length > 0:
                while i < min_length:
                    judge = strs[0][i]
                    for word in strs:
                        if word[i] != judge:
                            return common_prefix
                    common_prefix += judge
                    i += 1
        return common_prefix


print(Solution().longestCommonPrefix(["dog"]))