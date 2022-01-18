'''
本题要求计算1到n的奇数和。
输入格式:
在一行中给出一个正整数n
输出格式:
输出所求的和。
输入样例1:
5
输出样例1:
9
'''
sum=0
n=int(input())
if n % 2 ==0:
    n=n-1
    while n>0:
        sum=sum+n
        n=n-2
    print(sum)
else:
    while n>0:
        sum=sum+n
        n=n-2
    print(sum)