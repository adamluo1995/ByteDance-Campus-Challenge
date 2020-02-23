'''
题目：小明吃菜
思路：不跨过对角线，既是把方型分成两半，由于上下两部分是对称的，因此只要计算一半即可。
以上半部分为例，到达右上角，无论哪种最短路径都是n次上n次右。
如此一来，问题就是经典的动态规划问题。设NxN数组M记录到达(x,y)点共有几种走法，
可知M(0,0) = 0, M(*,0) = M(0,*) = 1，M(x,y) = M(x-1, y) + M(x, y-1)(对角线上特殊考虑)。
从上到下，从坐到右计算即可。
'''


def func(N):
    M = [[-1000 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        M[i][0] = 1
    for i in range(1, N):
        for j in range(1, i+1):
            if i != j:
                M[i][j] = M[i-1][j] + M[i][j-1]
            else:
                M[i][j] = M[i][j-1]
    return 2 * M[N-1][N-1]


def main():
    N = 5
    print(func(N))


if __name__ == "__main__":
    main()
