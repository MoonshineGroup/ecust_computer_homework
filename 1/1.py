choice = input("请输入您的选择1、2或其他：") #不转换成int防止用户输入非数字字符
if choice == "1":
    total = float(input("请输入红包金额："))
    n = int(input("请输入红包个数："))
    one = total / n
    print("红包总金额为：%.2f" % one)
elif choice == "2":
    from random import randint#也可以import random /random.randint 但不推荐，用什么就导入什么

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
