if __name__ == '__main__':
    n = int(input().strip())
    for i in range(1, n + 1):
        divisor = 1
        temp = i
        while temp >= 10:
            divisor *= 10
            temp //= 10
        num = i
        while divisor:
            digit = num // divisor
            print(digit, end='')
            num %= divisor
            divisor //= 10
