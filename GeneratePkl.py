# -*- coding:utf-8 -*-
import cPickle
import sqlite3 #测试

AppList = [u'TIM',u'猎豹浏览器',u'Anaconda',u'网易云音乐']
AppDict = {u'TIM':0,u'猎豹浏览器':1,u'Anaconda':2,u'网易云音乐':3}
ExeDict = {u'F:\\TIM\\Bin\\TIM.exe':0,
           u'F:\\猎豹chorm\\liebao\\6.0.114.14266\\liebao.exe':1,
		   u'F:\\Anaconda2\\Uninstall-Anaconda2.exe':2,
		   u'F:\\网易云\\CloudMusic\\cloudmusic.exe':3}
vocab = [AppList,AppDict]
cPickle.dump(ExeDict,open('exeMap.pkl','w'))
cPickle.dump(vocab,open('vocab.pkl','w'))

#测试区
f = open('exeMap.pkl','r')
ExeDict = cPickle.load(f)
f.close()

connect = sqlite3.connect('qs.db')
cursor = connect.cursor()
cursor.execute("SELECT id,process_name,exe_path FROM message WHERE id = 681")
records = cursor.fetchall()
print ExeDict[records[0][2]]