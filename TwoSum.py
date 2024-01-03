class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            #create a variable; save current number at the index
            urhere = nums[i] #calling nums wherever the index is when the for loop is running
            for j in range (0,len(nums)):
                if i != j:
                    if nums[j] + nums[i] == target: 
                        return [i,j] 
