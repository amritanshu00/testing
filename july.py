from math import ceil
def ans(n,l):
    if l.count(l[0])==n:
        return 1
    elif n%2==0:
        return -1
    else:
        d=l[1]-l[0]
        flag=0
        for i in range(1,len(l)-1):
            if l[i+1]-l[i]!=d:
                flag=1
                break
        if flag==1:
            return -1
        else:
            return ceil(n/2)
         
        


for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))

    a=ans(n,l)
    if a==-1:
        print('Impossible')
    else:
        print(a)
        
