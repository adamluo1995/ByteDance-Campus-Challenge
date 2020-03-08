'''
题目：简单的数学运算
思路：真就简单的数学运算呗，但这个加减运算的符号变了，没必要吧集美。
'''


def cal(a, b, op):
    if op == '+':
        return a-b
    elif op == '-':
        return a+b
    elif op == '*':
        return a/b
    elif op == '/':
        return a*b


def func(seq):
    op_level = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, ')': 0}
    nums = []
    tmp = ''
    ops = ['(']
    seq += ')'
    for e in seq:
        if e in ['+', '-', '*', '/', ')']:
            if len(tmp) > 0:
                nums.append(float(tmp))
                tmp = ''
            while op_level[e] <= op_level[ops[-1]]:
                if ops[-1] == '(' and e == ')':
                    return int(nums.pop(-1))
                b = nums.pop(-1)
                a = nums.pop(-1)
                nums.append(cal(a, b, ops.pop(-1)))
            ops.append(e)
        else:
            tmp += e


def main():
    seq = '2.1-3*4-1/2*3'
    print(func(seq))


if __name__ == "__main__":
    main()
