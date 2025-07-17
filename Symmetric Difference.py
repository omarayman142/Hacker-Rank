# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s=set(input().split(" "))
m=int(input())
s2=set(input().split(" "))
x=s.symmetric_difference(s2)
for num in sorted(x,key=int):
    print(num)
