# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         n=len(nums)
#         for i in range(n):
#             for j in range(i+1,n):
#                 if nums[i]==nums[j]:
#                     return True
#         return False            
# # it takes time:O(n.n) and time O(1)

class Solution:
    def containsDuplicate(nums):
        hash=set()
        for i in range(len(nums)):
            if nums[i] in hash:
                return True
            else:
                hash.add(nums[i])
        return False  

#this took time:o(n),space:o(n)                  
