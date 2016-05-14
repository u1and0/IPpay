'''
## IPpay ver1.2.1

__UPDATE1.2.1__
plan={'050plus':[300,{'cell':[8,180],'fix':[16,60]}],
みたいにしてみたけどどう？
まだ途中

__UPDATE1.2__
'050Call'は月間通話料が315円を下回った場合は、315円を請求
050Callは2.5時間くらい話さないと315円から変動しない？

__UPDATE1.1__
携帯と固定電話を別々にグラフ化

__UPDATE1.0__
First commit

__USAGE__
Just build

__INTRODUCTION__
IP電話アプリの料金をグラフ化

__ACTION__
http://s-dentoku.mobile-runner.com/hikaku
の料金をグラフ化してくれる
planに料金表


__TODO__
FUCK!通話料が海外用の金額と間違えてたぜ
しかも携帯と固定で料金加算時間が異なる！
'''





timeSec=[i for i in range(14401)]
plan={'050plus':[300,{'cell':[8,180],'fix':[16,60]}],
		'fusionIP':[0,8,8,30],
		'LaLa Call':[100,8,18,60],
		'G-Call050':[280,8,16,60],
		'050Call':[0,2,2,60],
		'050free':[0,3.99,4.33,60],
		'ServersMan 050':[300,7.5,40,180],
		'BIGLOBEフォン・モバイル':[300,8,30,60],
		'FleaLine Light':[400,8,30,60],
		'BlueSIPフォン':[600,21,21,60]
		}
mode=['cell','fix']
'''
planのリストの中身
0. 月額基本料金
1. 通話料(携帯電話)
2. 通話料(固定電話)
3. 料金加算時間
'''




import matplotlib.pyplot as plt
for l in mode:    #携帯電話と固定電話にかける場合
	k=0
	for sev in plan.keys():    #planディクショナリ内の業者名称をforeach
		j,pay=0,[]
		for i in timeSec:    #秒数だけループ
			pay.append(plan[sev][0]+plan[sev][mode[l]]*j)    #料金をリストに追加
			if i%plan[sev][3]==0:j+=1    #料金計算。30秒加算か1分加算がある(リストの項目3で決められている)
		if sev=='050Call':
			for modify in range(len(pay)):
				if pay[modify]<315:
					pay[modify]=315
		plan[sev].append(pay)    #料金をplanディクショナリの値(リスト)に追加してキーから呼び出せるようにする
		plt.plot(list(map(lambda re: re/60,timeSec)),plan[sev][4],'-' if k<7 else '--',label=sev)
		k+=1    #グラフカウンタ
	plt.title(l)
	plt.legend(bbox_to_anchor=(1, 0.5), loc='best', borderaxespad=0,fontsize='small')
	plt.subplots_adjust(right=0.75)
	plt.xlabel('minuits')
	plt.ylabel('Yen')
	plt.show()


