#coding utf-8
def sanijao():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]

n = 0
for t in sanijao():#t应该是 sanjiao()的返回值
    print (t)
    n = n + 1
    if n == 10:
        break