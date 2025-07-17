if __name__ == '__main__':
    N = int(input())
    List=[]
for i in range(N):
    m=input()
    m=m.split()
    if m[0]=="insert":
        List.insert(int(m[1]),int(m[2]))
    elif m[0]=="print":
        print(List)
    elif m[0]=="remove":
        List.remove(int(m[1]))
    elif m[0]=="append":
        List.append(int(m[1]))
    elif m[0]=="sort":
        List.sort()
    elif m[0]=="pop":
        List.pop()
    elif m[0]=="reverse":
        List.reverse()
