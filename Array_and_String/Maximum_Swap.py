class Solution(object):
    # fail
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        i = 0
        dupli = []
        while i < len(num) - 1:
            if num[i] < num[i + 1]:
                sub = num[i+1:]
                rest_list = [p for p in sub]
                max_val = max(rest_list)
                back = len(sub) - 1
                while sub[back] != max_val:
                    back -= 1

                index = back + 1 + i
                
                forward = i
                while forward > 0 and num[forward-1] < max_val:
                    forward -= 1

                if dupli:
                    i = dupli.pop(0)
                temp = num[i]
                num = num[:i] + num[index] + num[i+1:]
                num = num[:index] + temp + num[index+1:]
                return int(num)

            elif num[i] == num[i + 1]:
                dupli.append(i)
                i += 1
            else:
                dupli = []
                i += 1
        return int(num)

assert Solution().maximumSwap(2736) == 7236
assert Solution().maximumSwap(9973) == 9973
assert Solution().maximumSwap(1993) == 9913