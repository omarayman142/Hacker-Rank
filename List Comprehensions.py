if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result = []  # Initialize an empty list to store valid coordinates
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if (i + j + k) != n:
                    result.append([i, j, k])  # Append valid coordinate as a sublist
    print(result)  # Print the entire list of lists
