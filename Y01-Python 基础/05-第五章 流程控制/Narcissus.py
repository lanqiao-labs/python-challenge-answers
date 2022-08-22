n = input('请输入一个三位数：')
num = int(n)
if (num % 10)**3 + (num//10 % 10)**3+(num//100 % 10)**3 == num:
    print(f"{n}是水仙花数")
else:
    print(f"{n}不是水仙花数")
