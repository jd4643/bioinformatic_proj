
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# def add_up(nums,target):
#     for i in range(len(nums)):
#         if nums[i]+nums[i+1]== target:
#             return [nums[i],nums[i+1]]
#     return 
# nums = [2,7,11,15]
# target = 18
# print(add_up(nums,target))

# def add_up(nums):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#           if nums[i] + nums[j] == target:
#              return [nums[i], nums[j]]
            
    #         if nums[i] + nums[j] == target:
    #             return [nums[i], nums[j]]
    # return None

# nums = [2, 7, 11, 15]
# print(add_up(nums))  # Output: [2, 16]

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1

def nums1_(nums1,m):
    result = m
    while m < len(nums1):
        for i in range(len(nums1)):
            nums1.append(i)
            result+=1
            break
    return nums1
    
nums1 = [1,2,3,0,0,0]
m = 3
print(nums1_(nums1,m))

            














              
              
     


         
    









    


