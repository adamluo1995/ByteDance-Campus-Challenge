'''
题目：街道办找撤硕
思路：立马想到的思路，O(2n)的复杂度应该问题不大8。
最近的撤硕要么在前面要么在后面，那就做两遍dp。
第一遍从前往后遍历，m1记录“只看前面，离当前位置最近的撤硕有多远”。
第二遍从后往前遍历，m2记录“只看后面，离当前位置最近的撤硕有多远”。
最后取min(m1,m2)。（实现的时候，从后往前遍历的过程中就包含了min）。
'''


def func(N, seq):
    m1 = [float('inf')] * N
    m2 = [float('inf')] * N
    m = [float('inf')] * N
    for i, e in enumerate(seq):
        if e == 'O':
            m1[i] = 0
        else:
            if i > 0:
                m1[i] = m1[i-1] + 1
    for i in range(N-1, -1, -1):
        if seq[i] == 'O':
            m2[i] = 0
        else:
            if i < N-1:
                m2[i] = m2[i+1] + 1
        m[i] = min(m1[i], m2[i])
    return m


def main():
    seq = 'XXOXXXXOOXXOXO'
    N = len(seq)
    print(' '.join([str(e) for e in func(N, seq)]))


if __name__ == "__main__":
    main()
