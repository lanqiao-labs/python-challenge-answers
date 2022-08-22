n = input("请输入一个四位数：")
num = int(n)
total = num % 10 + num//10 % 10 + num//100 % 10 + num//1000
print(f"{n}的各位之和是：" + str(total))
