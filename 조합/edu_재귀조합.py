def combination(data,r,mstr="",n=0):
    if r == 0:
        print(mstr)
        return
    if n == len(data):
        return
    #잡았을때
    combination(data,r-1,mstr+str(data[n]),n+1)
    #못잡았을때
    combination(data,r, mstr,n+1)




data = [1,2,3,4,5]
combination(data,3)