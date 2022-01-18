'''
本题目要求读入2个字符串，第一个为明文，第二个为密码。 请使用密码对明文进行加密，加密的规则是依次取明文和密码中的字符， 进行异或运算。一般密码长度比明文短。当密码的字符取完以后，重新从头部开始取字符。
输入格式:输入在一行中给出2字符串s, p
输出格式:输出异或加密的结果
输入样例:
在这里给出一组输入。例如：
Top secret: I have a friend who
123456
输出样例:
在这里给出相应的输出。例如：
e]CFSR@V@x[UCSSRG_T\WB^^
'''
s = input()
p = input()
ls = len(s)
lp = len(p)
key = ls//lp*p+p[:ls%lp]
password = []
for i in range(len(key)):
	password.append(chr(ord(key[i])^ord(s[i])))
print(''.join(password))