'''
本题要求计算1到n阶乘和：1！+ 2！+ ... + n!
输入格式:
在一行中给出一个正整数n
输出格式:
输出所求的和。
输入样例2:
3
输出样例2:
9
'''
n = int(input())
fac = 1
sum = 0
i = 1
while n >= i:
    fac = fac * i
    sum = sum + fac
    i = i + 1
print(sum)