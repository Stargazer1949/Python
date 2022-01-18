'''
本题要求在屏幕上水仙花数。 如果输入的数据不在指定范围内，提示错误信息。
输入格式:
在一行中给出两个正整数M和N ，其中 99<N<M<1000
输出格式:
输出有三行： 第一行： M到N的水仙花个数
第二行：M到N的水仙花的总和
第三行：M到N的水仙花数
输入样例1:
800 600
输出样例1:
该输入范围内没有水仙花数
输入样例2:
55  599
输出样例2:
输入范围不对
输入样例3:
370  100
输出样例3:
2
523
370 153
'''
m,n=map(int,input().split())
s=[]
h=0
l=0
if 99<n<m<1000:
    for i in range(n,m+1):
        a = i//100
        b = (i-a*100)//10
        c = (i-a*100-b*10)
        if i == pow(a,3)+pow(b,3)+pow(c,3):
            s.append(i)
            h=h+i
    l=len(s)
    s.reverse()
    if l==0:
        print("该输入范围内没有水仙花数")
    else:
        print(l)
        print(h)
        for x in s:
            print(x,end=' ')
else:
    print("输入范围不对")