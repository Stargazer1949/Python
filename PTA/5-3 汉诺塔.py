'''
汉诺塔（又称河内塔） 问题是印度的一个古老的传说。 开天辟地的神勃拉玛在一个庙里留下了三根金刚石的棒A、B和C，A上面套着n个圆的金片，最大的一个在底下，其余一个比一个小，依次叠上去，庙里的众僧不倦地把它们一个个地从A棒搬到C棒上，规定可利用中间的一根B棒作为帮助，但每次只能搬一个，而且大的不能放在小的上面。
僧侣们搬得汗流满面，可惜当n很大时这辈子恐怕就很搬完了。
聪明的你还有计算机帮你完成，你能写一个程序帮助僧侣们完成这辈子的夙愿吗？
输入格式:
输入金片的个数n。这里的n<=10。
输出格式:
输出搬动金片的全过程。并在结束的时候输出搬运的总次数
输入样例:
在这里给出一组输入。例如：
2
结尾无空行
输出样例:
在这里给出相应的输出。例如：
Move disk 1 from A to B
Move disk 2 from A to C
Move disk 1 from B to C
3
'''
def hanoi(n, a, b, c):
    global count
    count += 1
    if n == 1:
        print("Move disk {} from {} to {}".format(1,a,c))
    else:
        hanoi(n - 1, a, c, b)
        print("Move disk {} from {} to {}".format(n,a,c))
        hanoi(n - 1, b, a, c)
n=int(input())
count = 0
hanoi(n,'A','B','C')
print(count,end='')