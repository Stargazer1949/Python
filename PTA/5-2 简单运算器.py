'''
请设计用于四种基本数学(+-*/)运算的整数计算器。 用英文拼写出0-9，结果为整数。
输入格式:
两个数通过英文拼写的方式表达，运算符用+-*/表示加减乘除。 one + two
输出格式:
输出一个结果，结果是整数 3
输入样例:
在这里给出一组输入。例如：
one / two
输出样例:
在这里给出相应的输出。因为0.5的结果没有办法保存在整数中，所以结果是0
0
'''
dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
a,b,c=map(str,input().split())
m=dict[a]
n=dict[c]
if b == '/':
    print(m // n)
elif b == '+':
    print(m + n)
elif b == '-':
    print(m - n)
else:
    print(m * n)