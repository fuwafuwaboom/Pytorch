import random
import sys
import time

print('-----------------------------')
print('|                            |')
print('|     花有重开日，人无再少年     |')
print('|                            |')
print('|       欢迎来到人生模拟器       |')
print('|                            |')
print('-----------------------------')

while True:
    print("请设置初始属性（可用点数总和为20）")
    face = int(input("请输入颜值（1-10）："))
    strong = int(input("请输入体质（1-10）："))
    iq = int(input("请输入智力（1-10）："))
    home = int(input("请输入家境（1-10）："))

    # 校验输入是否合法
    if face < 1 or face > 10:
        print('颜值输入有误')
        continue
    if strong < 1 or strong > 10:
        print('体质输入有误')
        continue
    if iq < 1 or iq > 10:
        print('智力输入有误')
        continue
    if home < 1 or home > 10:
        print('家境输入有误')
        continue
    if face + strong + iq + home > 20:
        print('总属性值超过20！')

    # 输入都合法就结束循环
    print("初始属性输入完毕！")
    print(f"颜值：{face}，体质：{strong}，智力：{iq}，家境：{home}")
    break

point = random.randint(1,6) # random.randint函数可以生成随机数 random是python中的一个模块（别人写好的代码直接给我们来用）
if point % 2 == 1:
    gender = 'boy'
    print('你是个男孩')
else:
    gender = 'girl'
    print('你是个女孩')

point = random.randint(1,3) # random.randint函数可以生成随机数 random是python中的一个模块（别人写好的代码直接给我们来用）
if home == 10:
    print('你出生在北京，你的父母是高管政要')
    home += 1
    iq += 1
    face += 1
elif 7 <= home <= 9:
    if point == 1:
        print('你出生在大城市，父母是公务员')
        face += 2
    elif point == 2:
        print('你出生在大城市，父母是企业高管')
    else:
        print('你出生在大城市，父母是大学教授')
        iq += 2
elif 4 <= home <= 6:
    if point == 1:
        print('你出生在三线城市，父母是医生')
        strong += 1
    elif point == 2:
        print('你出生在镇上，父母是教师')
        iq += 1
    else:
        print('你出生在镇上，父母是个体户')
        home += 1
else:
    if point == 1:
        print('你出生在农村，父母是辛苦劳作的农民')
        strong += 1
        face -= 2
    elif point == 2:
        print('你出生在山里，父母是无业游民')
        home -= 1
    else:
        print('你出生在镇上，父母离婚')
        strong -= 1
        home -= 1
    print("你人生的基础属性是：")
    print(f"颜值：{face}，体质：{strong}，智力：{iq}，家境：{home}")

# 幼年阶段
print("------------")
print("|  幼年阶段  |")
print("------------")
for age in range(1, 11, 2):
    info = f'你今年{age}岁.'
    point = random.randint(1, 3)
    if strong < 3:
        info += '你病死了'
        print(info)
        print('游戏结束！')
        sys.exit(0)
    if home == 10:
        if age == 1:
            info += '你喝着乳娘的奶，免疫力得到提升'
            strong += 1
        if age == 3:
            info += '你和同伴同学玩耍'
        if age == 5:
            info += '你进入全国最好的幼儿园'
            iq += 1
        if age == 7:
            info += '你进入全国最好的小学'
            iq += 1
        if age == 9:
            info += '你认现任省委书记为干爹'
    elif gender == 'girl' and home <= 3 and point == 1:
        info += '你的家里人重男轻女思想非常严重，你被遗弃在路边，病亡夭折'
        print(info)
        print('游戏结束！')
        sys.exit(0)

    elif strong < 6 and point < 3:
        info += '你生了一场大病'
        if home >= 5:
            info += '你在父母的悉心照料下，康复了'
            strong += 1
            home -= 1
        else:
            info += '你的父母没精力管你，也不愿意花钱，你的身体更糟糕了'
            strong -= 1
    elif face <= 4 and age >= 7:
        info += '你长得太丑了，别的小朋友不喜欢你'
        if iq > 5:
            info += '你开始用学习填充自己'
            iq += 1
        else:
            if gender == 'boy':
                info += '你经常和别的小朋友打架'
                strong += 1
                iq -= 1
            else:
                info += '你被女生孤立，被男生欺负'
                strong -= 1
    elif iq < 5:
        info += '你看起来傻傻的'
        if home >= 8 and age >= 6:
            info +='你的父母把你送到更好的学校学习'
            iq += 1
        elif 4 <= home <= 7:
            if gender == 'boy':
                info +='你的父母鼓励你多运动，争取成为运动员'
                strong += 1
            else:
                info +='你的父母鼓励你多打扮自己'
                face += 1
        else:
            info += '你的父母经常吵架'
            if point == 1:
                strong -= 1
            elif point == 2:
                iq -= 1
            else:
                pass
    else:
        info += '你健康成长，平稳的度过了童年时期'
        if point == 1:
            info += '你因为喜欢运动，看起来更结实了'
            strong += 1
        elif point == 2:
            info += '你看起来更好看了'
            face += 1
        else:
            pass
    print(info)
    time.sleep(1)

print("你当前的人生属性是：")
print(f"颜值：{face}，体质：{strong}，智力：{iq}，家境：{home}")
time.sleep(1)
print('------------------------------------------')

