class Solution:
    def list_sub_string(self, string):
        sub = []
        for i in range(len(string)):
            for j in range(len(string)-i):
                start = i
                end = i + j
                sub.append(string[i:i+j+1])
        return sub


print(Solution().list_sub_string("helloworld"))
