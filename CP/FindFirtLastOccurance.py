def find(nums,target):
    pos=[]
    for i in range(len(nums)):
        if nums[i]==target:
            pos.append(i)
    if(len(pos)==0):
        pos.append(-1)
        pos.append(-1)
        return pos
    else:
        pos1=[]
        pos1.append(min(pos))
        pos1.append(max(pos))
        return pos1
nums=[2,4,5,7,3,2,4,5]
print(find(nums,2))
