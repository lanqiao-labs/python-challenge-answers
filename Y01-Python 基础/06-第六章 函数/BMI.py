def bmi(h, w):
    bmi = w/(h*h)
    if bmi < 18.5:
        print("体重过低")
    elif 24 > bmi >= 18.5:
        print("体重正常")
    elif 28 > bmi >= 24:
        print("超重")
    else:
        print("肥胖")


if __name__ == "__main__":
    h = float(input("请输入身高(m)："))
    w = float(input("请输入体重(kg)："))
    bmi(h, w)
