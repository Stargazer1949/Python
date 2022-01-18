'''
本题要求输入数组大小和数组中每一个元素，求该数组中第二小的数和数所在的位置。 如果输入的数据过少，提示错误信息。
输入格式:
数组大小M和数组中的元素 其中，1<M<100, 数组中的元素互不相等。
输出格式:
第二小数和对应的下标
输入样例1:
4
11 0 8 9
输出样例1:
8
2
输入样例2:
1
9
输出样例2:
输入的数据不符合题目要求
'''
a=int(input())
b=list(map(int,input().split()))
min1=0
min2=0
if 1<a<100:
    for i in range(len(b)):
        if b[i] < b[min1]:
            min2 = min1
            min1 = i
        elif b[i] < b[min2]:
            min2 = i
    print(b[min2])
    print(min2)
else:
    print("输入的数据不符合题目要求")