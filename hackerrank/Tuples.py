if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    s = list(integer_list)

    t = tuple(s)

    print(hash(t))
