'''
给出一个定义域范围[a,b)，求该范围内函数xsin(x) 的局部极小值x对应的坐标， 要求输出结果精确到小数点后2位。
输入样例:a,b 分别为
0, 13
输出样例:第一行是所求x的值，第二行是相应的局部极小值
4.91 11.09
-4.81 -11.04

样例解释，xsin(x) 在区间[0,13)上的两个局部极小值是 -4.81，-11.04 对应的x坐标是4.91和11.09.
'''
import math
a,b = map(eval,input().split(","))
def f(x):
    sinx = math.sin(x)
    f = x * sinx
    return f
value = []
position = []
c = [i/100 for i in range(a*100,b*100)]
for i in c:
    if f(i)<f(i-0.01) and f(i)<f(i+0.01):
        position.append(i)
        value.append(f(i))
del position[0]
del value[0]
for i in position:
    print("{:.2f}".format(i),end=' ')
print()
for i in value:
    print("{:.2f}".format(i),end=' ')