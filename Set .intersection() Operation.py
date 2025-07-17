# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
s=set(input().split(" "))
m=int(input())
s2=set(input().split(" "))
print(len(s.intersection(s2)))
