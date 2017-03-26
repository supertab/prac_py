# fun ： addPlayer、removePlayer、recordMoney、settleAcount
#修改字典是对全局进行修改--ok
#输入得分后显示提示信息--ok
#列表去重--ok
#disp改善--ok
#移除玩家要情况记录--ok
#load后新添加玩家（中途添加玩家）--ok
#移除玩家出现非法输入--ok
import pickle
def addPlayer(pDict = {},pList = []):
        hadPlay = 0
        if len(pList)!=0:
                hadPlay = len(pDict[pList[0]])      
        while True:
                player = input('输入玩家名字,逐个添加，回车输入，0返回菜单：')
                if '0' == player:
                        break;
                if '' != player:
                        if player not in pList:
                                pList.append(player)
                                print('成功添加玩家 %s'%player)
                        else:
                                print('该玩家已存在,请重新',end='')
                else:
                        print('输入不能为空,请重新',end='')
        print('游戏玩家有：',end = '')
        for i in pList:
                pDict.setdefault(i,[0]*hadPlay)
                print(i,end = ' ')
        print()
        dispDict(pDict,pList)

def removePlayer(pDict={},pList=[]):
        print('----游戏中的玩家有----')
        for i in pList:
                print(i,end = ' ')
        print('\n--------------------')
        while True:
                quitPlayer = input('输入需要离开的玩家,输入0返回菜单：')
                if '0' == quitPlayer:
                        break;
                try:
                        pList.pop(pList.index(quitPlayer))
                        pDict.pop(quitPlayer)
                        print('玩家-',quitPlayer,'-已移除')
                except:
                        print('玩家-',quitPlayer,'-不存在',end=',')
                        continue
        #清除得分记录
        for player in pDict:
                pDict[player].clear()

def recordMoney(pDict,pList,Times):
        print('---输入得分---')
        print('说明:输家输入数值（正数），赢家得分输入0，程序将自动计算')
        tempList = []
        while True:
                try:
                        for player in pList:
                                tmp = input('%s得分:'%player)
                                while not tmp.isdigit():
                                        tmp = input('%s得分:'%player)
                                tempList.append(int(tmp))

                        winner = -sum(tempList)#列表求和
                        tempList[tempList.index(0)] = winner
                        break
                except ValueError:
                        print('输入有误：赢家得分用 0 表示...')
                        tempList.clear()#添加不成功则清除缓存

        tempList = list( map(lambda x:-x,tempList ))#对列表元素取反
        for player in pList:
                pDict.setdefault(player).append(tempList[
                        pList.index(player)])#把每局玩家的得分存入字典中
        print('---记录成功---')
        dispDict(pDict,pList,dispTms=Times)
def settleAccount(pDict,pList):
        print('\n--------[说明]比例表示：1积分 = 多少元--------')
        print('------[例]规定 1积分 = 1角,则比例 = 0.1------')
        while True:
                try:
                        unitY =float(input('游戏结算,输入比例（元）：'))
                        break
                except ValueError:
                       print('输入数字,',end = '')
        dispDict(pDict,pList)
        print('----------游戏结算----------')
        for player in pList:
                print(player,'：',end='')
                print('%.2f 元'%(sum(pDict[player])*unitY))
                #pDict[player].clear()
                
#打印全部，打印最新添加的一行
def dispDict( pDict,pList,dispTms='allDict' ):
        print('-------------玩家信息如下-------------')
        #打印全部列表
        if 'allDict'== dispTms:
                dispTms = len(pDict[pList[0]])
                for player in pList:
                        print('\t',player,end='')#打印玩家名字
                print()
                for i in range(dispTms):
                        print('第%d局：'%(i+1),end='')
                        for player in pList:
                                print('\t',pDict[player][i],end='')
                        print()
        else:#打印一行
                for player in pList:
                        print('\t',player,end='')#打印玩家名字
                print()
                print('第%d局：'%(dispTms),end='')
                for player in pList:
                        print('\t',pDict[player][dispTms-1],end='')
                print()
        print('--------------------------------------')

def saveDict( pDict ):
        savFile = open('playerDict.pkl','wb')
        pickle.dump(pDict,savFile)
        savFile.close()
        print('保存成功,文件名为 playerDict.pkl ...')
        #return 0

def loadDict():
        pList = []
        loadFile = open('playerDict.pkl','rb')
        pDict = pickle.load(loadFile)
        loadFile.close()
        for player in pDict:
                pList.append(player)
        print('加载成功...')
        dispDict(pDict,pList)
        return(pDict,pList)
#先打印所有列表，再根据提示进行修改,修改之后需要重新计算winner的得分
#输入需要在索引范围内
def modifyDict(pDict,pList):
        dispDict(pDict,pList)
        print('例如:修改第2位玩家在第1轮的得分,输入列号:2,行号:1')
        colMax = len(pDict)
        rowMax = len(pDict[pList[0]])
        #处理非法输入
        while True:
                colDict = input('输入列号 1~%d：'%colMax)
                if colDict.isdigit():
                        colDict = int(colDict)
                        if 0 < colDict <= colMax:
                                break
                        else:
                                print('超出范围,',end='请重新')
                else:
                        print('输入数字,',end='请重新')
                
                colDict = print('输入数字,请重新输入列号:')
       
        while True:
                rowDict = input('输入行号 1~%d：'%rowMax)
                if rowDict.isdigit():
                        rowDict = int(rowDict)
                        if 0 < rowDict <= rowMax:
                                break
                        else:
                                print('超出范围,',end='请重新')
                else:
                        print('输入数字,',end='请重新')
                
        newScore = int(input('将 -{player}- 在第-{playTimes}-局的得分修改为：'.format(
                player = pList[colDict-1],playTimes = rowDict)))
        scoreGap = newScore - pDict[pList[colDict-1]][rowDict-1]#新旧得分之差

        for winner in pList:
                if pDict[winner][rowDict-1] > 0:
                        pDict[winner][rowDict-1] -= scoreGap
                        break
        pDict[pList[colDict-1]][rowDict-1] = newScore

        print('---------------修改成功---------------')
        dispDict(pDict,pList)
        print()

titleProg = '''{front}
*{midOne}—— 游戏计分器 v1.0 ——{midOneEnd}*
*{midTwo}    by:zooo {midTwoEnd}*
{end}'''.format(front = '*'*42,end='*'*42,midOne=' '*8,
                midOneEnd=' '*7,midTwo=' '*22,midTwoEnd = ' '*6)

zSkill = '''---HIDE FUNCTION---
{front}
在菜单中直接输入下列字符，可以实现对应功能
  save：保存文件（文件的后缀名为pkl）
  load：读取保存的文件（pkl文件需要与exe文件在同一目录下）
  modify：修改数据（例如:修改第2位玩家在第1轮的得分,输入列号:2,行号:1）
  disp：显示游戏记录
  clear：清除所有数据
{end}
'''.format(front = '*'*60,end = '*'*60)

proFun = '''{front}
说明1-> 程序的功能：记录每轮游戏各玩家的分数（适用于棋牌类,进行多轮的游戏）,并进行结算
        --还有一些隐藏功能哦~(input z on table will display)
说明2-> 使用步骤：1.添加参与游戏玩家 2.每轮游戏结束后,选择-游戏记录-记录玩家得分
                3.游戏结束后,选择-游戏结算-,输出每位玩家的最终得分
{end}'''.format(front='-'*75,end='-'*75)

#print(zSkill)
print(titleProg)
ifItem = '0'
playTimes = 0
playerList = []#打印玩家
playerDict = {}#统计玩家数据
while ifItem != 'q':
        try:
                item = input('-------------------菜单-------------------\n\
1.添加玩家 2.减少玩家 3.游戏记录 4.游戏结算 \nq.退出程序 h.使用帮助：')
                ifItem = item
                if 'z' == ifItem:
                        print(zSkill)
                elif 'h' == ifItem:
                        print(proFun)
                elif 'load' == ifItem:
                        temp = loadDict()
                        playerDict = temp[0]
                        playerList = temp[1]
                        for player in playerList:
                                playTimes = len(playerDict[player])
                                break
                havePlayer = len(playerDict)
                
                if item not in '1qhz' and 0 == havePlayer:
                        print('请先添加玩家...')
                        int('zooo')
                        
                if 'save' == ifItem:
                        saveDict( playerDict )
                elif 'disp' == ifItem:
                        dispDict(playerDict,playerList)
                elif 'modify' == ifItem:
                        modifyDict(playerDict,playerList)
                elif 'clear' == ifItem:
                        playerList.clear()
                        playerDict.clear()
                        print('清除记录成功！')
                item = int(item)
                if 1 == item:
                        addPlayer(playerDict,playerList)#playerDict.updata(addPlayer())
                elif 2 == item:
                        isRemove = input('移除玩家会清除游戏记录,请先进行结算,是否继续（Y/N）:')
                        if isRemove in 'yY':
                                removePlayer(playerDict,playerList)
                elif 3 == item:
                        playTimes += 1
                        recordMoney(playerDict,playerList,playTimes)
                elif 4 == item:
                        settleAccount(playerDict,playerList)#结算后需要将value清空
        except:
                print(end='')
