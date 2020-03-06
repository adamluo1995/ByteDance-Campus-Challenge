'''
题目：顺序做题
思路：尝试动态规划，一维不行，二维没试出来，但复杂度肯定是O(nm)。遂将问题简单化，做点小变化，即完成第i个问题的情况下，前面最多还可以做多少道。
显然，在剩余时间有限的情况下，选耗时最少的做就能做最多。
因此，先对a排序，之后对每一道题，在完成它的情况下，按a的顺序不断地塞进耗时最少且序号在它前面地题目即可。复杂度O(n^2)，比dp好些。
'''


def func(n, m, a):
    a_sort = list(enumerate(a))
    a_sort.sort(key=lambda x: x[1])
    r = [i for i in range(n)]
    for i in range(n):
        num, v = a_sort[i]
        res_m = m - v
        for j in range(n):
            if a_sort[j][0] < num:
                if res_m >= a_sort[j][1]:
                    res_m -= a_sort[j][1]
                    r[num] -= 1
                else:
                    break
    return r


def main():
    n = 4
    m = 10
    a = [4, 8, 2, 8]
    print(' '.join([str(e) for e in func(n, m, a)]))


if __name__ == "__main__":
    main()
