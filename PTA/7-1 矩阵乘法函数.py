'''
设计一个Python函数，计算两个矩阵（二维列表）的乘积。
函数接口定义：
def multiply(a,b,p,q,r)
a是一个p行q列的二维列表；b是一个q行r列的二维列表； 应返回矩阵p行r列的结果矩阵。
裁判测试程序样例：
p = int(input())
q = int(input())
r = int(input())
a = [[random.randint(0,10) for x in range(q)] for y in range(p)]
b = [[random.randint(0,10) for x in range(r)] for y in range(q)]
c = multiply(a,b,p,q,r)  #调用执行读者写的函数
rst = True
#由出题者书写的正确函数计算返回的标准答案
answerTypical = multiply1(a,b,p,q,r)
for i in range(p):
    for j in range(r):
        if c[i][j] != answerTypical[i][j]:
            rst = False
            break
print(rst)
#测试程序的正确输出
True
测试程序输入样例：
3
2
1
测试程序输出样例：
True
'''
import random
def multiply(a,b,p,q,r):
    Matrix = [[random.randint(0,0) for x in range(r)] for y in range(p)]
    k=0
    while k!=r:
        for i in range(p):
            v=0
            for j in range(q):
                v += a[i][j]*b[j][k]
            Matrix[i][k]=v
        k+=1
    return Matrix