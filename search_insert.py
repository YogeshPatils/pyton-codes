'''
this function returns the index number
nums sorted integer list, 
target the number to be searched or inserted if not found
'''
def searchInsert(nums, target): 
        if target in nums:
            return nums.index(target)
        else:
            if target<nums[(len(nums)//2)]:
                i=0
                while i<(len(nums)//2)+1:
                    if target<nums[i]:
                        return i
                    i+=1
            else:
                if target>nums[-1]:
                    return len(nums)
                else:
                    i=len(nums)//2
                    while i<len(nums):
                        if target<nums[i]:
                            return i
                        i+=1
