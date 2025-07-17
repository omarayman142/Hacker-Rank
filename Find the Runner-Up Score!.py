if __name__ == '__main__':
    n = int(input())
    arr =list( map(int, input().split()))
    max1=-101
    max2=-101
    for i in range(n):
        if(arr[i]>max1):
            max2=max1
            max1=arr[i]
        elif arr[i]<max1 :
            if arr[i]>max2:
                max2=arr[i]
print(max2)
