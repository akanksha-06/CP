def ishappy(n):
    already=[]
    l=list(str(n))
    if n==1:
        return True
    sum1=0
    while sum1!=1:
        for i in l:
            sum1+=(int(i)**2)
        if sum1==1:
            return True
        else:
            if sum1 in already:
                return False
            already.append(sum1)
            l=list(str(sum1))
            sum1=0
print(ishappy(19))
        
