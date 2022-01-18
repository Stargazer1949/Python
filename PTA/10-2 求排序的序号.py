'''
程序输入共2行，第1行有一个整数n[1,1000]，表示共有n个整数；第2行是空格分隔的n个不同的整数(int范围) 编写程序输出每个数按从小到大排序后的排名
输入样例:在这里给出一组输入。例如：
5
8 2 6 9 4
输出样例:在这里给出相应的输出。例如：
4 1 3 5 2

解释:从小到大排序后，8排第4位，2排第1位，6排第3位,9排在第5位，4排在第2位
'''
l = int(input())
m = input().split(' ')
n = []
for i in m:
    n.append(int(i))
m = list(n)
n.sort(reverse = False)
a = []
for i in m:
    b = n.index(i) + 1
    a.append(b)
for i in a:
    print(i, end=' ')