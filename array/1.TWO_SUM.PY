# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]


# using this soln takes nth time n no ,which means O(n.n)
def twoSumusingpointers(num,target):
  for i in range (len(num)):
        for j in range(i+1,len(num)):
            if (num[i]+num[j] == target):
                return [i,j]
  return []    
       
num=[2,7,11,15]
target=9
result= twoSumusingpointers(num,target)
print (result)

# using hash map method,best case complexity time complexity=O(n)
def twoSum(nums,target):
  dict={}
  for i,n in enumerate (nums):
        diff =target - n
        if diff in dict:
            return [dict[diff],i]
        dict[n]=i
nums=[2,1,5,3]
target=4
result= twoSum(nums,target)
print (result)
        

  