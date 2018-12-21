class Solution(object):
    def longestPalindrome(self, s):
        seen = []
        max_palindrome = s[0] if s else ""


        for idx, c in enumerate(s):
            if seen:
                if c == seen[-1]:
                    max_palindrome = self.compare_pal(self.check_even(seen, s[idx:]), max_palindrome)

                if len(seen) >  1 and c == seen[-2]:
                    max_palindrome = self.compare_pal(self.check_odd(seen, s[idx:]), max_palindrome)

                seen.append(c)
            else:
                seen.append(c)

        return max_palindrome
    
    def compare_pal(self, pal_1, pal_2):
        if len(pal_1) > len(pal_2):
            return pal_1
        
        else:
            return pal_2
    
    def check_even(self, seen, s):
        seen_pivot = len(seen) - 1
        s_pivot = 0
        result = []
        output = ""
        
        while s_pivot < len(s) and seen_pivot > -1 and seen[seen_pivot] == s[s_pivot]:
            result.append(seen[seen_pivot])
            seen_pivot -= 1
            s_pivot += 1
        
        for i in result[-1::-1]:
            output += i
        
        for i in result:
            output += i
        
        return output
        
    def check_odd(self, seen, s):
        result = []
        head = seen[-1]
        seen = seen[:-1]
        seen_pivot = len(seen) - 1
        s_pivot = 0
        output = ""
        
        while s_pivot < len(s) and seen_pivot > -1 and seen[seen_pivot] == s[s_pivot]:
            result.append(seen[seen_pivot])
            seen_pivot -= 1
            s_pivot += 1
        
        for i in result[-1::-1]:
            output += i
        
        output += head
        
        for i in result:
            output += i

        return output





























    def longestPalindrome_not_working(self, s):
        """
        :type s: str
        :rtype: str
        """
        seen = []
        go_check = False
        temp_palin = []
        addition_c = []
        head = None
        max_head = None
        max_palin = []

        if not s:
            return ""

        if len(s) == 1:
            return s
        
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            
            else:
                return s[0]

        for c in s:
            if seen:
                if len(seen) > 1 and seen[-2] == c:
                    go_check = True
                    head = seen.pop()
                    temp_palin.append(seen.pop())


                elif seen[-1] == c:
                    go_check = True
                    head = None
                    temp_palin.append(seen.pop())
                
                
                else:
                    if go_check:
                        if head:
                            if len(max_palin) < len(temp_palin) + 1:
                                max_palin = temp_palin
                                max_head = head
                        
                        else:
                            if len(max_palin) < len(temp_palin):
                                max_palin = temp_palin
                                max_head = head
    
                        go_check = False
                        seen = []
                        temp_palin = []
                        head = None
                        seen.append(c)
                    
                    else:
                        seen.append(c)
            
            else:
                if go_check:
                    if head:
                        if len(max_palin) < len(temp_palin) + 1:
                            max_palin = temp_palin
                            max_head = head
                    
                    else:
                        if len(max_palin) < len(temp_palin):
                            max_palin = temp_palin
                            max_head = head

                    go_check = False
                    seen = []
                    temp_palin = []
                    head = None
                    seen.append(c)
                
                else:
                    seen.append(c)
        

        result = ""
        for i in range(len(max_palin) - 1, -1, -1):
            result += max_palin[i]
        
        if max_head:
            result += max_head
        
        for i in max_palin:
            result += i

        return result


assert Solution().longestPalindrome("babad") == "bab" or Solution().longestPalindrome("babad") == "aba"
assert Solution().longestPalindrome("cbbd") == "bb"
assert Solution().longestPalindrome("ccc") == "ccc"