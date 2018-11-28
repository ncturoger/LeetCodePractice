class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        s_len = len(s)
        for i in range(0, int(s_len/2)):
            self.swap(i, s_len-1-i, s)
        
        return "".join(s)
    
    def swap(self, i, j, arr):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

print(Solution().reverseString("Hello"))