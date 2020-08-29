def resolve():
    '''
    code here
    '''
    D, T, S = [int(item) for item in input().split()]

    if D / S <= T:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    resolve()
