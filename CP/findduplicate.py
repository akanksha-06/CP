#method1
def findduplicate(nums):
    seen=set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
nums=[1,4,3,6,2,4,7]
print(findduplicate(nums))

'''
here time and space complexity is order of n
where as in sum2-sum1 method time complexity is order of n but space coplexity
is order of 1 as we use space for only sum variable
'''

def method2(nums):
    cnt=[0]*len(nums)+1
    for num in nums:
        cnt[num]+=1
        if cnt[num]>1:
            return num
    return len(nums)
def method3(nums):
    for num in nums:
        idx=abs(num)
        if nums[idx]<0:
            return num
        nums[idx]=-nums[idx]
    return len(nums)
def method4(nums):
    #slow and fast floyd cycles detection approach
    slow=nums[0]
    fast=nums[0]
    while True:
        slow=nums[slow]
        fast=nums[nums[fast]]
        if slow==fast:
            break
    return slow
#method5
'''
sort the list and traverse if nums[i]==nums[i-1] return nums[i]
'''

    



    
