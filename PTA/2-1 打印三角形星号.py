'''
用户输一个一个正整数，显示一个三角形星号。
输入样例1:
3
输出样例1:
  *
 * *
* * *
'''
n = int(input())
for i in range(n):
    str1=str(" " * (n - 1 - i))
    str2=str("* " * (i + 1))
    print(str1, end='')
    print(str2.rstrip())