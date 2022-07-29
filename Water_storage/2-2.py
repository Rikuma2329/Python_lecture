input = list(input())

while input != [] and input[0] != '\\':     #左側はバックスラッシュが来るまで水は貯まらないので削除
    input.pop(0)

while input != [] and input[-1] != '/':     #右側はスラッシュが来るまで水は貯まらないので削除
    input.pop()

depth = 0       #はじめの谷の左端を基準の深さ0
base = []       #凸（/\ か　/_）の部分の高さを格納するリストbase
baseidx = []     #凸の部分がリストinputの何インデックス目の後に当たるかを格納するリストbaseidx
vol = []        #各谷ごとの貯水量を格納するリストvol
base.append(depth)
baseidx.append(-1)

for i in range(0, len(input)):
    if i == len(input) - 1 or (input[i] == '/' and (input[i + 1] == '\\' or input[i + 1] == '_')):      #各谷の右端になり得る位置
        depth -= 1
        base.append(depth)      #そのときの深さ
        baseidx.append(i)       #その地点のインデックス
    
    elif input[i] == '\\':
        depth += 1
    
    elif input[i] == '/':
        depth -= 1

while len(base) > 1:
    cul = 0
    for i in range(1, len(base)):
        if base[0] >= base[i]:      #base[0]と同じ深さ or それより高い（深さが負）とその点まで1つの谷
            cul = i
            break
    else:
        cul = base.index(min(base[1 : ]))       #base[0]より深い点しかない → それ以降で最も浅いところまでが1つの谷

    water = 0       #1つの谷の貯水量water
    depth = 0       #1つの谷の深さdepth（左端が基準）
    check = input[baseidx[0] + 1 : baseidx[cul] + 1]        #1つの谷の構造をcheckに格納
    mosthigh = max(0, base[cul] - base[0])      #1つの谷でどの高さまで水が貯まるかを示すmosthigh
    #print(base)
    #print(check)

    while check != []:
        if check[0] == '\\':
            if depth >= mosthigh:
                water += (1/2) + (depth - mosthigh)
            depth += 1
            check.pop(0)

        elif check[0] == '_':
            if depth > mosthigh:
                water += depth - mosthigh
            check.pop(0)

        elif check[0] == '/':
            if depth > mosthigh:
                water += (depth - mosthigh) - (1/2)
            depth -= 1
            check.pop(0)
        
    vol.append(int(water))      #1つの谷の貯水量waterをvolに挿入

    del base[0 : cul]       #探索したbaseの部分を削除
    del baseidx[0 : cul]        #探索したbaseidxの部分を削除

print(sum(vol))
for i in range(0, len(vol)):
    print(vol[i], end = ' ')



    