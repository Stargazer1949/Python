'''
图像匹配问题。给出若干幅图像，图像的数据可以用矩阵表示。图像的数据范围是[0,255]。给出起始的图像x，在剩下任一图像中任选图像y，计算x的最后一列和y的第一列的欧氏距离。剩下图像中这种欧氏距离最小的图像是是最匹配的图像。假设最匹配图像为y0, 继续在余下的图像中寻找和y0最匹配的图像。重复这个过程，直到没有图像剩下。
现在给出p幅图像的数据，依次编号为1,2，...,p。 每幅图像的大小是m×n. 假设第一幅图像设置为编号x, 1≤x≤p. 按照前一段图像最匹配描述，计算最匹配的序列。
输入格式:
第一行输入四个整数m,n,p,x
第二行到到底m*p行，每一行有n个数据。 依次表示编号为1,2，...,p的图像数据。
输出格式:
输出最匹配序列，包括起始编号x
输入样例:
2, 2, 3, 2
33, 44
33, 44
55, 33
55, 33
44, 99
44, 99
输出样例:
2 1 3

样例说明， 2, 2, 3, 2 表示图像大小为2×2, 共3幅图像， 起始图像编号是2。
第一幅图像数据
33, 44
33, 44
第二幅图像数据
55, 33
55, 33
第三幅图像数据
44, 99
44, 99
输出结果 2 1 3 表明起始图像x编号为2，图像2最匹配的是1，图像1最匹配的是3。
'''
import numpy as np
temp = [eval(x) for x in input().split(',')]
m = temp[0]
n = temp[1]
p = temp[2]
first = temp[3]
imgs_3d = np.zeros((m, n, p))
for i in range(m * p):
    k = i // m
    j = i % m
    temp = [eval(x) for x in input().split(',')]
    if j == 0:
        temps = [temp]
    else:
        temps.append(temp)
    if len(temps) == m:
        imgs_3d[:, :, k] = np.array(temps)
# 计算两幅图拼接的距离d(i,j), i,j相邻，i前j后
d = np.zeros((p, p))
for i in range(n):
    for j in range(n):
        x = imgs_3d[:, -1, i]
        y = imgs_3d[:, 0, j]
        z = x - y
        d[i, j] = np.linalg.norm(z)
        if i == j:
            d[i, j] = np.inf  # 碎纸片只能和其他碎纸片相邻
# 求矩阵d每一行的最小值所对应的下标
ind = np.argmin(d, axis=1)
sorted_ind = [first - 1]
while len(sorted_ind) < len(ind):
    j = sorted_ind[-1]
    k = ind[j]
    if k not in sorted_ind:
        sorted_ind.append(k)
    else:
        d[j, k] = np.inf
        ind = np.argmin(d, axis=1)
sorted_ind2 = [i + 1 for i in sorted_ind]
for i in sorted_ind2:
    print(i, end=' ')