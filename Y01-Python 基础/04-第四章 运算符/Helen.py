a = float(input("请输入第一个边长："))
b = float(input("请输入第二个边长："))
c = float(input("请输入第三个边长："))
p = (a+b+c)/2
s = (p*(p-a)*(p-b)*(p-c))**0.5
print(f"三角形的面积是{s:.2f}")
