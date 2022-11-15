def searchInsert(self, nums, target):
        c=0
        for i in nums:
            if target<=i:
                return c
            else:
                c+=1
        return len(nums)         
   
 #happy coding😊
