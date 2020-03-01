'''
题目：最大子串和
思路：经典动态规划问题。记m[i]为以i结尾的子串的最大和，则m[i] = max(m[i-1]+v[i], v[i]), 即要么是连着前面，要么就是自己。最后取m中的最大值即可。
'''


def func(nums):
    max_sum = -float('inf')
    m = [-1] * len(nums)
    for i, n in enumerate(nums):
        if i == 0:
            m[i] = n
        else:
            m[i] = max(m[i-1]+n, n)
            if m[i] > max_sum:
                max_sum = m[i]

    return max_sum


def main():
    nums = [-2, 11, -4, 13, -5, -2]
    print(func(nums))


if __name__ == "__main__":
    main()
