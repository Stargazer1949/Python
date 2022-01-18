'''
利用泰勒展开求cos函数： cos(x)=
输入格式:
输入两个数，一个x, 一个k
输出格式:
求cos(x)的泰勒展开级数前k项和
输入样例:在这里给出一组输入。例如：
1.047
40
输出样例:小数点后精度到6位。
0.500171
'''
import math
def fa(a):
    b=1
    while a!=1:
        b*=a
        a-=1
    return b
def taylor(x,k):
    a=1
    count=1
    for i in range(1,k):
        if count%2!=0:
            a-=(x**(2*i))/fa(2*i)
        else:
            a+=(x**(2*i))/fa(2*i)
        count+=1
    print("{:.6f}".format(a))
    return a
x=eval(input())
k=int(input())
taylor(x,k)