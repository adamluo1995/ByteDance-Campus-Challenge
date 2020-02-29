'''
题目：最少硬币
思路：类似于"上楼梯"的动态规划问题，做些小改动，并记录下每一步的选择。
'''


def func(vs, t):
    m = [[] for _ in range(t+1)]
    for i in range(1, t+1):
        min_len = 1000
        for v in vs:
            if i - v >= 0 and len(m[i-v]) + 1 < min_len:
                m[i] = m[i-v] + [v]
                min_len = len(m[i])
    return m[t]


def main():
    vs = [1, 2, 5, 10, 50]
    t = 38
    print(func(vs, t))


if __name__ == "__main__":
    main()
