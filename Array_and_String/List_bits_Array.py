class Solution:
    def list_bit(self, n):
        self.arr = []
        self.get_bit([], n)
        return self.arr
        

    def get_bit(self, bit, n):
        if len(bit) == n:
            self.arr.append(bit)
            return

        self.get_bit(bit + [0], n)
        self.get_bit(bit + [1], n)
            

print(Solution().list_bit(4))