class Solution(object):
    def containsDuplicate(self, nums):
        di={}
        for i in nums:
            if i not in di:
                di[i]=1
            else:
                return True
        return False
