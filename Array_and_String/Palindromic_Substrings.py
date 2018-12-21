class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        palindromic_count_dict = dict()
        total = 0

        for i in range(len(s)):
            for j in range(len(s) - i):
                sub = s[i:i+j+1] 
                if palindromic_count_dict.get(sub):
                    palindromic_count_dict[sub] += 1
                else:
                    if self.check_pa(sub):
                        palindromic_count_dict[sub] = 1
        
        for s, count in palindromic_count_dict.items():
            total += count
        
        return total
    

    def check_pa(self, s):
        if len(s) == 1:
            return True
        for i in range(int(len(s)/2)):
            if s[i] != s[len(s)-i-1]:
                return False
        return True


assert Solution().countSubstrings("abc") == 3
assert Solution().countSubstrings("aaa") == 6



        
            

        
                
