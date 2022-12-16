from random import randint
import time,sys

# 玩家
class Player:

    def __init__(self,stoneNumber):
        self.stoneNumber = stoneNumber # 灵石数量
        self.warriors = {}  # 拥有的战士，包括弓箭兵和斧头兵

# 战士
class Warrior:

    # 初始化参数是生命值
    def __init__(self, strength):
        self.strength = strength

    # 用灵石疗伤
    def healing(self, stoneCount):
        # 如果已经到达最大生命值，灵石不起作用，浪费了
        if self.strength == self.maxStrength:
            return

        self.strength += stoneCount

        # 不能超过最大生命值
        if self.strength > self.maxStrength:
            self.strength = self.maxStrength


# 弓箭兵 是 战士的子类
class Archer(Warrior):
    # 种类名称
    typeName = '弓箭兵'

    # 雇佣价 100灵石，属于静态属性
    price = 100

    # 最大生命值 ，属于静态属性
    maxStrength = 100


    # 初始化参数是生命值, 名字
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # 和妖怪战斗
    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 20
        elif monster.typeName== '狼妖':
            self.strength -= 80
        else:
            print('未知类型的妖怪！！！')



# 斧头兵 是 战士的子类
class Axeman(Warrior):
    # 种类名称
    typeName = '斧头兵'

    # 雇佣价 120灵石
    price = 120

    # 最大生命值
    maxStrength = 120


    # 初始化参数是生命值, 名字
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # 和妖怪战斗
    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 80
        elif monster.typeName== '狼妖':
            self.strength -= 20
        else:
            print('未知类型的妖怪！！！')

# 鹰妖
class Eagle():
    typeName = '鹰妖'

# 狼妖
class Wolf():
    typeName = '狼妖'

# 森林
class Forest():
    def __init__(self,monster):
        # 该森林里面的妖怪
        self.monster = monster

print('''
***************************************
****           游戏开始             ****
***************************************


加载中请等待...
'''

)

# 森林数量
forest_num = 7

# 森林 列表
forestList = []

# 为每座森林随机产生 鹰妖或者 狼妖
notification = '前方森林里的妖怪是：\n '  # 显示在屏幕上的内容
for i in range(forest_num):
    typeName = randint(0,1)
    if typeName == 0:
        forestList.append( Forest(Eagle()) )
    else:
        forestList.append( Forest(Wolf()) )

    notification += \
        f'第{i+1}座森林里面是：{forestList[i].monster.typeName} \n '

# 显示 妖怪信息
print(notification,end='')

print('\n')


#10秒后删除屏幕信息
time.sleep(10)
for i in range(len(notification)):
	sys.stdout.write('\b')
	time.sleep(0.02)
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')
print('\n')	#通过换行删除屏幕信息



#创建玩家
Player = Player(1000)
print(f'你目前拥有{Player.stoneNumber}灵石')

#雇佣战士流程
def hireWarriors():

	menu = '''
	请选择雇佣兵种
	0 - 雇佣完成，退出
	1 - 弓箭兵
	2 - 斧头兵
	:'''
	while True:
		choice = input(menu)

		if choice not in['0','1','2']:
			print('输入错误，请重新输入！')
			continue


		if choice == '0':	#退出雇佣流程
			return

		if choice == '1':	#雇佣弓箭兵
			hireClass = Archer

		else:				#雇佣斧头兵
			hireClass = Axeman

		if hireClass.price > Player.stoneNumber:
			print(f'灵石不足以雇佣当前战士，你目前拥有{Player.stoneNumber}灵石')
			continue

		#给雇佣的战士命名
		while True:
			warriorName = input('请给该战士起名：')
			if not warriorName:		#玩家没有输入内容
				continue
			if warriorName in Player.warriors:
				print('该名字已被占用，请重新输入')
				continue
			break

		#雇佣到战士
		Player.warriors[warriorName] = hireClass(warriorName)

		#支付灵石
		Player.stoneNumber -= hireClass.price

		print(f'雇佣成功，你当前拥有{Player.stoneNumber}灵石')

#雇佣弓箭兵和斧头兵
hireWarriors()

#打印出麾下战士和灵石的情况
def printlnfo():
	print('\n你当前拥有战士如下：')
	for name,warrior in Player.warriors.items():
		print(f'{name}:{warrior.typeName}生命值{warrior.strength}')

print('\n\n******开始挑战******')



count = 0
for no,forest in enumerate(forestList):
	#如果战士队列为空，则游戏挑战失败
	if not Player.warriors:
		print('您麾下没有战士，游戏结束')
		exit()

	print(f'\n\n >>>现在到了第{no+1}座森林')
	count += 1

	if no+1>7:
		print(f'恭喜您挑战成功，你当前拥有{Player.stoneNumber}灵石')
		break


	#派出战士，森林作战
	while True:
		while True:
			warriorName = input('你要派出作战的战士是？')
			if warriorName not in Player.warriors:
				print('没有该战士，请重新选择出战士兵')
				continue
			break

		warrior = Player.warriors[warriorName]

		print(f'当前森林里是{forest.monster.typeName}')

		warrior.fightWithMonster(forest.monster)

		print(f'经过战斗，你的战士{warriorName},生命值还有{warrior.strength}')

		#如果生命值小于等于0，该战士便牺牲了，从队伍中消失
		if warrior.strength <= 0:
			print('该战士已光荣牺牲')
			Player.warriors.pop(warriorName)
			# 没有战胜怪物，本关没有通过
			continue

		#战士生还，过关
		else:
			break

	input('\n\n成功通过此森林，按回车键进入下一森林...')

	#过关后，选择给战士疗伤

	while True:
		printlnfo()

		op = input('''\n请输入疗伤战士名字和灵石数量，格式为：姓名+20
直接回车退出疗伤:''')

		if not op:
			break

		if op.count('+') !=1:
			print('输入格式错误，请重新输入')
			continue

		name,stoneCount = op.split('+')
		name = name.strip()




	#输出最终玩家的灵石数目
	if count == 7:

		print(f'\n >>>恭喜您挑战成功，您最终剩余{Player.stoneNumber}灵石。')


