'''
假设美元对人民币的汇率固定为6.4，请写程序完成美元和人民币互换问题。
输入格式:
如果用户输入16.5￥表示输入的人民币16.5元，请将人民币换成美元
如果用户输入16.5＄表示输入的美元16.5元，请将美元转换为人民币
输出格式:
输出对应货币的数量并加上对应货币符号 比如：1.00＄
其中数据精确到小数点后两位
'''
money_convert = input("")
if money_convert[-1] in ['￥']:
    d = eval(money_convert[0:-1])/6.4
    print("{:.2f}＄".format(d))
elif money_convert[-1] in ['＄']:
    r = 6.4*eval(money_convert[0:-1])
    print("{:.2f}￥".format(r))
else:
    print("输入格式不对")