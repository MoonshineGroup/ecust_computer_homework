choice = input("请输入您的选择1、2或其他：")
if choice == "1":
    one = float(input("请输入红包金额："))
    n = int(input("请输入红包个数："))
    total = one * n
    print("红包总金额为：%.2f" % total)
elif choice == "2":
    from random import randint
    target = randint(1, 6)
    guess = int(input("请输入您的猜测："))
    if guess<target:
        print("您猜大了，色子数是%d"%target)
    elif guess>target:
        print("您猜小了，色子数是%d"%target)
    else:
        print("您猜对了！")
else:
    print("您的输入有误！！")
