if __name__ == '__main__':
    N = int(input())
    lst = []
    while N > 0:
        str = list(input().split())

        if str[0] == 'print':
            print(lst)
        elif str[0] == 'insert':
            lst.insert(int(str[1]), int(str[2]))
        elif str[0] == 'remove':
            lst.remove(int(str[1]))
        elif str[0] == 'append':
            lst.append(int(str[1]))
        elif str[0] == 'sort':
            lst.sort()
        elif str[0] == 'reverse':
            lst.reverse()
        elif str[0] == 'pop':
            lst.pop()

        N -= 1
