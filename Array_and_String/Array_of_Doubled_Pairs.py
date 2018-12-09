from collections import Counter

class Solution(object):
    def canReorderDoubled(self, A):
        A=sorted(A)
        tmp={}
        idx=len(A)-1
        #print(A)
        while idx>=0 and A[idx]>0:
            i=A[idx]
            idx-=1
            if 2*i in tmp and tmp[2*i]>0:
                    tmp[2*i]-=1
            else:
                tmp[i]=tmp.get(i,0)+1
        for i in tmp:
            if tmp[i]!=0:
                return False
        tmp={}
        idx=0
        while idx<len(A) and A[idx]<0:
            i=A[idx]
            idx+=1
            if 2*i in tmp and tmp[2*i]>0:
                tmp[2*i]-=1
            else:
                tmp[i]=tmp.get(i,0)+1
        for i in tmp:
            if tmp[i]!=0:
                return False
        return True


assert Solution().canReorderDoubled([4,-2,2,-4]) == True
assert Solution().canReorderDoubled([2,1,2,1,1,1,2,2]) == True
