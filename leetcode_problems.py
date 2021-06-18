#containers duplicate

#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def containsDuplicate(self, nums: List[int]) -> bool:
    
    # no_dups = []
        
        #TOO SLOW!
#         for i in nums:
#             if i not in no_dups:
#                 no_dups.append(i)
#             else:
#                 return True
            
#         return False



        #a little better
#         nums.sort()
    
#         checker = 0

#         for i in range(0, len(nums) - 1):
#             if nums[i] == nums[i + 1]:
#                 checker += 1
            
#         return checker > 0


      nums.sort()
    
      checker = 0

      for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                checker += 1
                if checker > 0:
                    return True
            
      return False


#Valid anagram
#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
def isAnagram(self, s: str, t: str) -> bool:
        
      if len(s) != len(t): return False
        
      s_list = []
      for char_s in s:
            #put all char in a list
            s_list.append(char_s)
        
        #loop through t
      for char_t in t:
            #if t is in s we remove it 
            if char_t in s_list:
                s_list.remove(char_t)
        
        #if the len of the list is 0 that means its an anagram
      return len(s_list) == 0


#Find pivot index 
#Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
# Return the leftmost pivot index. If no such index exists, return -1.

def pivotIndex(self, nums: List[int]) -> int: 
        
        #works on some cases
        
#         left_sum = 0
#         right_sum = 0
        
#         for i in range(0, len(nums)):
#             left_sum += nums[i]
            
#             for j in range(i + 1, len(nums)):
#                 right_sum += nums[j]
        
            
#             if left_sum == right_sum:
#                 return i + 1
            
#             right_sum = 0
        
        
#         return -1

        left_list = []
        right_list = []
        left_sum = 0
        right_sum = 0
        
        
        for i in range(0, len(nums)):
            
            left_list.append(nums[i])
            # minus the current index because its not included in the pivot
            left_sum = sum(left_list) - nums[i]
            
            for j in range(i + 1, len(nums)):
                #calculating total sum of right side to compare with left
                right_list.append(nums[j])
                
            right_sum = sum(right_list)
            if left_sum == right_sum:
                return i
            
            #resetting the right array
            right_list = []
            
        return -1;
    
    

    #working on a better solution
#     total_left_sum = 0
#     total_right_sum = sum(nums)
    
#     last_index = len(nums) - 1
    
#     for i in range(len(nums)):
#         total_left_sum += nums[i]