x = int(input("请输入一个非负整数:"))
factorial = 1
if x<0:
    print("请输入非负整数。")
else:
    for i in range(1,x+1):
        factorial *= i
    print(f"{x}的阶乘是:{factorial}")