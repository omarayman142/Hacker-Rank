# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split(" "))
sum=0
no_n= input().split(" ")
A= set(input().split(" "))
B= set(input().split(" "))
for i in no_n:
    if i in A:
        sum =sum+1
    elif i in B:
        sum =sum-1
print(sum)
