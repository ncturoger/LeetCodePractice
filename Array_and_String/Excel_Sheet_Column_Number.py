class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = [
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
            "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
            "U", "V", "W", "X", "Y", "Z"
            ]
        num_dict = dict()
        result = 0

        for idx, word in enumerate(words):
            num_dict[word] = idx + 1

        digit = 1
        i = len(s) - 1
        while i > -1:
            result += digit * num_dict[s[i]]

            digit *= 26
            i -= 1

        return result





assert Solution().titleToNumber("A") == 1
assert Solution().titleToNumber("AB") == 28
assert Solution().titleToNumber("ZY") == 701