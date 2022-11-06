def fb(n):
    if n <=1:
        return n
    else:
        return (fb(n-1)+fb(n-2))


def fb2(n,second_last,last):
    if n-1 ==0:
        return second_last
    new_last = second_last + last
    second_last = last
    return fb2(n-1,second_last,new_last)

    
n=21
#for i in range(n):
    #print (fb(i))

print (fb2(n,0,1))
