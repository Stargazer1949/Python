'''
每一个列表中只要有一个元素出现两次，那么该列表即被判定为包含重复元素。
编写程序：对n行字符串进行处理，一行字符串构成一个列表。程序判定每一个列表中是否包含重复元素。最后统计包含重复元素的行数与不包含重复元素的行数。
输入格式:
输入n，代表接下来要输入n行字符串。
然后输入n行字符串，字符串之间的元素以空格相分隔。
输出格式:
True=包含重复元素的行数
False=不包含重复元素的行数
输入样例:
5
1 a 3 c 5
a 3 c 5 d
b 2 3 b 1
x 2 w 2 w
a 1 1 1 1
输出样例:
True= 3
False= 2
'''
n = int(input())
false = 0
true = 0
for i in range(n):
    line = input()
    list1 = []
    list1 = line.split()
    if len(list1) == len(set(list1)):
        false += 1
    else:
        true += 1
print("True= {}".format(true))
print("False= {}".format(false))