def findmissingsmallestpositive(nums):
    n=max(nums)
    m=-1
    for i in range(1,n+2):
        if i in nums:
            continue
        else:
            '''m=1'''
            return i
            break
    '''if m==-1:
        m=max(nums)+1
    return m'''
nums=[1,2,0,5,3,4]
print(findmissingsmallestpositive(nums))

'''
    from collections import counter
    def missing(nums,n):
        c=counter(nums)
        for i in range(len(nums)):
            if i+1 not in c:
                return 1+1
        return len(nums)+1'''



'''
    import heapq
    def missing(nums):
        heap=[]
        for i in nums:
            if i>0:
                heap.append(i)
        missing_pos=1
        while heap:
        smallest=heapq.heappop(heap)
            if smallest==missing_pos:
                missing_pos+=1
            elif smallest>missing_pos:
                return missing_pos
        return missng_pos
'''


