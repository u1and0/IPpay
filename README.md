## IPpay ver2.0
__UPDATE2.0__
グラフを並べて表示
準備段階として`plan={'050plus':{'base':300,'fix':[8,180,[]],'cell':[16,60,[]]},`ディクショナリ in ディクショナリのリストの第2要素をプロットするように変更


__UPDATE1.4__
auの通話料追加
毎月10分くらいは通話してるのかな

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
none
