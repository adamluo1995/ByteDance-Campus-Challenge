'''
题目：一大堆需求
思路：经典贪心问题，选择当前时间点可完成的需求中，工期最短的。
先证明，该问题的最优解的第一项，一定是工期最短的解。
用反证法，若该问题的解的第一项不是工期最短的解，意味着有一个工期更短的需求，不在解中。
那么就可以把这个需求替换解的第一项，则解的长度（完成数量）不变，也是最优解。
因此，工期最短的解放在第一位，一定是最优解。
以此类推，可以证明每次选择可选需求中工期最短的，一定是最优解。
'''


def func(w_arr, d_arr):
    now = 1
    cnt = 0
    wd_arr = [e for e in zip(w_arr, d_arr)]
    wd_arr.sort(key=lambda x: x[0])
    while len(wd_arr) > 0:
        w, d = wd_arr.pop(0)
        if now + w <= d+1:
            cnt += 1
            now += w
    return cnt


def main():
    w = [4, 6, 2, 4, 7, 9]
    d = [7, 9, 10, 12, 5, 9]
    print(func(w, d))


if __name__ == "__main__":
    main()
