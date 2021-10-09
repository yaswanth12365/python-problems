	#as per number of zeroes do the operation
	res=[] 
    cnt=0
    for i in range(len(nums)):
        if nums[i]==0:
            cnt+=1
        
    if cnt>1:

        for i in range(len(nums)):
            res.append(0)
        return res
    elif cnt==0:
        prod=1
        for i in range(len(nums)):
            prod*=nums[i]
        for i in range(len(nums)):
            if nums[i]!=0:
                res.append(prod//nums[i])
    elif cnt==1:
        prod=1
        for i in range(len(nums)):
            if nums[i]!=0:
                prod*=nums[i]
        for i in range(len(nums)):
            if nums[i]!=0:
                res.append(0)
            else:
                res.append(prod)
        
    return res
