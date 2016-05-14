'''
## IPpay ver1.1

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
'050Call'は月間通話料が315円を下回った場合は、315円を請求
'''





timeSec=[i for i in range(3601)]
plan={'050plus':[300,9,29,60],
		'fusionIP':[0,8,8,30],
		'LaLa Call':[100,6,28,60],
		'G-Call050':[280,5,10,60],
		'050Call':[0,2,2,60],
		'050free':[0,3.99,4.33,60],
		'ServersMan 050':[300,7.5,40,180],
		'BIGLOBEフォン・モバイル':[300,8,30,60],
		'FleaLine Light':[400,8,30,60],
		'BlueSIPフォン':[600,21,21,60]
		}
'''
planのリストの中身
0. 月額基本料金
1. 通話料(携帯電話)
2. 通話料(固定電話)
3. 料金加算時間
'''




import matplotlib.pyplot as plt
mode={'cell':1,'fix':2}
for l in mode.keys():    #携帯電話と固定電話にかける場合
	k=0
	for sev in plan.keys():    #planディクショナリ内の業者名称をforeach
		j,cell,fix=0,[],[]
		for i in timeSec:    #秒数だけループ
			cell.append(plan[sev][0]+plan[sev][mode[l]]*j)    #料金をリストに追加
			if i%plan[sev][3]==0:j+=1    #料金計算。30秒加算か1分加算がある(リストの項目3で決められている)
		plan[sev].append(cell)    #料金をplanディクショナリの値(リスト)に追加してキーから呼び出せるようにする
		plt.plot(list(map(lambda re: re/60,timeSec)),plan[sev][4],'-' if k<7 else '--',label=sev)
		k+=1    #グラフカウンタ
	plt.title(l)
	plt.legend(bbox_to_anchor=(1, 0.5), loc='best', borderaxespad=0,fontsize='small')
	plt.subplots_adjust(right=0.75)
	plt.xlabel('minuits')
	plt.ylabel('Yen')
	plt.show()


