'''
给出一个矩阵，求最大值及其下标
输入格式:
第一行：矩阵大小,m*n
第二行到m+1行,表示矩阵的具体数据
输出格式:
输出最大值
输入样例:在这里给出一组输入。例如：
3,3
1,2,3
4,5,6
2,3,1
输出样例:在这里给出相应的输出。例如：
6 2 3

样例说明：矩阵大小为3*3，最大值是6，位置是2行3列。
'''
a,b = map(int,input().split(','))
list = []
array = []
for i in range(a):
    list = input().split(',')
    new_list = [];
    for n in list:
        new_list.append(int(n))
    array.append(new_list)
max_a = 0
for i in range(len(array)):
    if max(array[i]) > max(array[max_a]):
        max_a = i
max_b = max(array[max_a])
m = max_a
n = array[max_a].index(max_b)
print("{} {} {}".format(max_b,m+1,n+1))