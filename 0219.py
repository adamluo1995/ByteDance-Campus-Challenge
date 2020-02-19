'''
秘密通信
思路：观察规律即可，用不上算法的东西。
'''


def xor(seq):
    tmp = 0
    for i in seq:
        tmp += i
    return 0 if tmp % 2 == 0 else 1


def func(N, K, seq):
    r = [-1] * N
    k = 0
    for i in range(len(r)):
        r[i] = xor([seq[i]] + r[i-k:i])
        if k < K - 1:
            k += 1
    return r


def main():
    N, K = 7, 4
    seq = [1, 1, 1, 0, 1, 0, 0, 1, 1, 0]
    print(func(N, K, seq))


if __name__ == "__main__":
    main()
