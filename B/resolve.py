def resolve():
    '''
    code here
    '''

    S = input()
    T = input()

    if T in S:
        print(0)
    else:
        res = 0
        for i in range(len(S) - len(T) +1):
            temp = S[i:]
            max_num = 0
            for j in range(len(T)):
                if temp[j] == T[j]:
                    max_num += 1
            res = max(res, max_num)

        print(len(T) - res)


if __name__ == "__main__":
    resolve()
