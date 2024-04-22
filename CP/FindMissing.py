def findmissing(nums):
    for i in range(len(nums)+1):
        if i in nums:
            continue
        else:
            return i
            break
nums=[3,2,5,6,1,0]
print(findmissing(nums))


'''
    def findmissing(nums,n):
        n=len(nums)
        sum1= int((n*(n+1))/2)
        sum2=0
        for i in nums:
            sum2+=i
        print(sum1-sum2)
'''
''' for finding duplicate numbers sum2-sum1'''

        
