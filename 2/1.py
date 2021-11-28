# 运行前，你不仅需要安装pypi包`qrcode`，还需要安装`pillow`
import qrcode
import os
from math import sin,cos,pi
from turtle import pendown,penup,goto,done,speed,setup,pencolor
print("1、个人信息二维码  2、四叶草的动态绘制")
print("3、自动关机小程序  3、师生举行募捐活动")
a=int(input("请输入你的选择（按0退出)："))
while a!=0:
    if a==1:
        img=qrcode.make("个人信息")
        img.save("个人信息.png")
        print("个人信息二维码已生成")
    elif a==2:
        setup(600,600)
        speed(100)
        wh=300
        hh=300
        pencolor("green")
        t=0
        penup()
        goto(wh*2/3*cos(2*t)*cos(t),hh*2/3*cos(2*t)*sin(t))
        pendown()
        while t<2*pi:
            goto(wh*2/3*cos(2*t)*cos(t),hh*2/3*cos(2*t)*sin(t))
            t=t+0.01
        done()
    elif a==3:
        t=int(input("您希望多少秒之后关机："))
        os.system("shutdown -s -t %d"%t)
        m=int(input("是否希望取消关机（按1取消）："))
        if m==1:
            os.system("shutdown -a")
    elif a==4:
        sum=0
        i=0
        while True:
            money=int(input("请输入您的捐款，输入0结束："))
            if money==0:
                break
            sum=sum+money
            i=i+1  
        ave=sum/i
        print("捐款人数为%d，平均金额为%d"%(i,ave))
    else:
        print("输入错误！")
    a = int(input("请输入你的选择（按0退出)："))
print("感谢你的使用")




