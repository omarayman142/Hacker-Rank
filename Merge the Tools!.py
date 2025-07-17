def merge_the_tools(string, k):
    t = []
    for i in range(0, len(string), k):
        t.append(string[i:i+k])
    for i in range(len(t)):
        t[i] = ''.join(sorted(set(t[i]), key=t[i].index))
    print(*t, sep='\n')

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)