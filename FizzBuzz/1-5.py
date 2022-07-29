def fizzbuzz(n):
    flexresult = ''
    for i in range(0, len(rule), 2):
        if n % rule[i] == 0:
           flexresult += rule[i + 1] 
    
    if flexresult == '':
        return str(n)
    else:
        return flexresult

Input = input()     

Input = Input.replace(':', ' ')     #入力された文字列Inputの':'を半角スペースに置き換える。

rule = Input.split()        #Inputを空白文字で区切ってリスト化。

n = int(rule[-1])       #リストruleの一番最後の要素を取り出す。

rule.pop()      #リストruleの一番最後の要素を消去する。

for i in range(0, len(rule), 2):        #リストruleの偶数インデックス（倍数指定の数字が入っている）の要素をint化
    rule[i] = int(rule[i])

data = list(range(1, n + 1))        #最小値1、最大値nの整数リストdataを用意

result = map(fizzbuzz, data)        #リストdataを関数fizzbuzzで加工

print(list(result))