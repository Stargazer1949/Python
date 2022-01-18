'''
本题要求在屏幕上显示M行字母三角形。 如果输入的数据不在指定范围内，提示错误信息
输入格式:
在一行中给出一个正整数M，要求1<=M <=10
输出格式:
输出M行的三角形字母
输入样例1:
3
输出样例1:
A
AB
ABC
'''
s = "ABCDEFGHIJ"
n = int(input())
if 0< n <= 10:
    for i in range(n):
        print(s[0:i+1])
else:
    print("输入范围不对",end='')