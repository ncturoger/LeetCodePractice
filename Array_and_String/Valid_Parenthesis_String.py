class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        special_stack = []
        str_stack = []

        for idx, c in enumerate(s):
            if c == "(":
                str_stack.append(idx)
            
            elif c == "*":
                special_stack.append(idx)
            
            elif c ==")":
                if str_stack:
                    str_stack.pop()
                
                else:
                    if special_stack:
                        special_stack.pop()
                    
                    else:
                        return False
        

        if str_stack:
            i = 0
            while i < len(str_stack):
                find = False
                for item in special_stack:
                    if str_stack[i] < item:
                        special_stack.remove(item)
                        find = True
                        break

                if not find:
                    return False
                i += 1
            return True
                    
        else:
            return True


assert Solution().checkValidString("()") == True
assert Solution().checkValidString("(*)") == True
assert Solution().checkValidString("(*))") == True
assert Solution().checkValidString("(*()") == True
assert Solution().checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*") == False
assert Solution().checkValidString("(())(())(((()*()()()))()((()()(*()())))(((*)()") == False
