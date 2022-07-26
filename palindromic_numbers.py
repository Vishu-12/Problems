#question:-
#https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/palindromic-numbers-7/


#Solution:-

def palindrom(a:int,b:int)->int:
    count=0
    for i in range(a,b+1):
        s=str(i)
        # print(s)
        re=s[::-1]
        # print(re)
        if s==re:
            count=count+1
    return count



t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    result=palindrom(a,b)
    print(result)