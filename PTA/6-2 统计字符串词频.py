'''
从键盘读入由仅由英文构成的多行文本，借助于字典统计其中每个单词出现的次数。然后按输出最高频的词汇。
要求：
所有单词不区分大小写，输出时按小写格式输出；
需要排除常见的英文符号，如! , : ?等英文符号，即这些符号不应作为单词的构成部分;
输出： 最高频的词汇 最高频的词汇出现次数
输入格式:
行数n 第1行内容 第2行内容 .... 第n行内容
输出格式:
最高频的词汇 最高频的词汇出现次数
输入样例:在这里给出一组输入。例如：
5
 Mr. and Mrs. Dursley, of number four, Privet Drive,
　　Mr. Dursley was the director of a firm
　　The Dursleys had everything they
　　When Mr. and Mrs. Dursley woke up on the dull, gray Tuesday
　　None of them noticed a large, tawny owl flutter past the window.
输出样例:在这里给出相应的输出。例如：
the 4
'''
l = int(input())
str0 = ''
for i in range(l):
    str0 += input() + ' '
str0 = str0.lower()
a = "\',.?!;0123456789"
for i in a:
    str0 = str0.replace(i, "")
dic = {}
words = str0.split()
for i in words:
    dic[i] = dic.get(i,0)+1
ls = list(dic.items())
ls.sort(key=lambda x:x[1],reverse=True)
word, count = ls[0]
print("{} {}".format(word, count),end='')