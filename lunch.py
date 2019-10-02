for _ in range(int(input())):
    n=int(input())
    if n<10:
        print(n)
    elif str(n)[-1]=='0':
        print(n-1)
    else:
        print(n-(n%10)-1)
        
        
        
