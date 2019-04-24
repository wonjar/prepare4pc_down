# -*- coding:utf-8 -*-
import sys
import sqlite3
import cPickle
#参数1：从数据库中取记录的起始id
CurrentId = int(sys.argv[1])
EndId = int(sys.argv[2])
#参数2：结束id，取到此id后不再继续读取

#上次匹配上字典了的应用
CurrentApp = -1
#应用序号的列表
AppNum = []

#读取exeMap.pkl和vocab.pkl，洗数据需要查的表
f = open('exeMap.pkl','r')
ExeDict = cPickle.load(f)
f.close()

f2 = open('vocab.pkl','r')
vocab = cPickle.load(f2)
f2.close()
AppList = vocab[0]
AppDict = vocab[1]
#连接数据库
connect = sqlite3.connect('qs.db')
cursor = connect.cursor()

while (CurrentId < EndId):
    #注意参数的数据类型是否匹配！动态类型一时爽，修起bug火葬场
    cursor.execute("SELECT id,process_name,exe_path FROM message WHERE id = ?",(str(CurrentId),))
    records = cursor.fetchall()
    #查表决定抄下来还是丢掉
    if (records[0][2] in ExeDict):
        appNumber = ExeDict[records[0][2]]
        #不要重复记录
    	if appNumber != CurrentApp:
    	    AppNum.append(appNumber)
            CurrentApp = appNumber
    #处理完一条之后，取下一条记录
    CurrentId += 1
#输出的是没有按一组20个破开的初步数据，后续再处理。
cPickle.dump(AppNum,open('RealUnsplit.pkl','w'))