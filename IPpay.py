'''
## IPpay ver1.3

__UPDATE1.3__
`plan={'050plus':{'base':300,'fix':[8,180],'cell':[16,60],'payList':[]},`として基本料金と固定電話、携帯電話の通話料をネスとされたディクショナリにした
`base:基本料金,fix:[通話料,料金加算時間],cell:[通話料,料金加算時間],payList:[グラフに表示するリスト]`
__UPDATE1.2.1__
`plan={'050plus':[300,{'fix':[8,180],'cell':[16,60]}],`みたいにしてみたけどどう？
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





timeSec=[i for i in range(0,7201,30)]
plan={'050plus':{'base':300,'fix':[8,180],'cell':[16,60],'payList':[]},
		'fusionIP':{'base':0,'fix':[8,30],'cell':[8,30],'payList':[]},
		'LaLa Call':{'base':100,'fix':[8,180],'cell':[18,60],'payList':[]},
		'G-Call050':{'base':280,'fix':[8,180],'cell':[16,60],'payList':[]},
		'050Call':{'base':0,'fix':[7.62,180],'cell':[14.29,60],'payList':[]},
		'050free':{'base':0,'fix':[8,180],'cell':[5.5,30],'payList':[]},
		'ServersMan 050':{'base':300,'fix':[8,180],'cell':[16,60],'payList':[]},
		'BIGLOBEフォン・モバイル':{'base':300,'fix':[8,180],'cell':[15.9,60],'payList':[]},
		'FleaLine Light':{'base':400,'fix':[8,180],'cell':[16,60],'payList':[]},
		'BlueSIPフォン':{'base':600,'fix':[20,60],'cell':[20,60],'payList':[]}
		}
mode=['fix','cell']
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
			pay.append(plan[sev]['base']+plan[sev][l][0]*j)    #料金をリストに追加
			if i%plan[sev][l][1]==0:j+=1    #料金計算。30秒加算か1分加算がある(リストの項目3で決められている)
		if sev=='050Call':
			for modify in range(len(pay)):
				if pay[modify]<315:
					pay[modify]=315
		plan[sev]['payList']=pay    #料金をplanディクショナリの値(リスト)に追加してキーから呼び出せるようにする
		plt.plot(list(map(lambda re: re/60,timeSec)),plan[sev]['payList'],'-' if k<7 else '--',label=sev)
		k+=1    #グラフカウンタ
	plt.title(l)
	plt.legend(bbox_to_anchor=(1, 0.5), loc='best', borderaxespad=0,fontsize='small')
	plt.subplots_adjust(right=0.75)
	plt.xlabel('minuits')
	plt.ylabel('Yen')
	plt.show()


