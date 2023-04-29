def nums1_(nums1,m):
    result = m
    while m < len(nums1):
        for i in range(len(nums1)):
            nums1.append(i)
            break
    return nums1
    
nums1 = [1,2,3,0,0,0]
m = 3
print(nums1_(nums1,m))