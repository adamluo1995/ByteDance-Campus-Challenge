'''
题目：文件传输
思路：老动态规划了。先把数据按开始时间排序，之后从前往后遍历，p[i]记录“第i个位置会产生多少重叠”。
则，最大的堆积就是最大的“重叠+文件数”，最晚结束时间就是“最后一个任务的重叠+最后一个任务的耗时”。
'''


def func(n, d):
    p = [0] * n
    d.sort(key=lambda x: x[0])
    for i in range(1, n):
        p[i] = max(0, d[i-1][1] - d[i][0] + d[i-1][0] + p[i-1])
    max_v = 0
    for i in range(n):
        max_v = max(p[i]+d[i][1], max_v)
    ft = p[n-1] + d[n-1][1] + d[n-1][0]
    return ft, max_v


def main():
    n = 3
    d = [[1, 3], [2, 3], [3, 3]]
    ft, max_v = func(n, d)
    print(str(ft)+' '+str(max_v))


if __name__ == "__main__":
    main()
