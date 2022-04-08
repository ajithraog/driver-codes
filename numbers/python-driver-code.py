def solve(N:int)  ->str:
    s=str(N)
    div=lens(s)//2
    if int(N)%2==0:
        left=s[0:div]
        right=s[div:]
    else:
        left=s[0:div]
        right=s[div+1:] 
    if int(left)> int(right):
       return "magic number"
    else:
       return "normal number"
 T=int(input())
 for i in range(T):
     test_case=input()
     answer=solve(test_case)
    print(answer)

