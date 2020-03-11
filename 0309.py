'''
题目：很多新人
思路：数连通分量问题，用并查集实现。如果将每对导师新人视作编号为1至N的结点,且若两对导师新人可通过一次交换即满足要求，则连上边。
如此一来，可以组成一个无向图，存在若干连通分量。每一次交换最多减少一个连通分量，因此最少交换次数是 N-连通分量个数。
'''


def find(x, parent):
    if parent[x] != x:
        x = parent[x]
    return x


def uni(x, y, parent, size):
    x = find(x, parent)
    y = find(y, parent)
    if size[x] <= size[y]:
        parent[x] = y
        size[y] += size[x]
    else:
        parent[y] = x
        size[x] += size[y]


def func(matrix):
    N = int(len(matrix) * len(matrix[0]) / 2)
    parent = [i for i in range(N)]
    size = [1] * (N)
    cnt = 0
    for row in matrix:
        for i in range(0, len(row), 2):
            x, y = int((row[i]-1) / 2), int((row[i+1]-1) / 2)
            uni(x, y, parent, size)
    for i, e in enumerate(parent):
        if i == e:
            cnt += 1
    return N-cnt


def main():
    matrix = [[1, 3], [2, 4]]
    print(func(matrix))


if __name__ == "__main__":
    main()
