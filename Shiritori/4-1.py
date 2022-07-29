import os

shiritorilist = []          #しりとり結果を格納するリスト

def import_data():
    uselist = []

    for path, dirs, files in os.walk('./files'):        #ファイル名のみuselistに格納
        if(files != []):
            for i in range(0, len(files)):
                uselist.append(files[i])

    return(uselist)

def pair(wordlist):
    pairlist = []

    for i in range(0, len(wordlist)):           #wordlistから最初の文字、最後の文字だけ抜き出す
        pairlist.append((wordlist[i])[:1] + (wordlist[i])[-1:])

    return(pairlist)

def start_check(wordlist):
    count = {}
    for i in range(97, 123):        #アルファベット（A~Z）を辞書のキーに設定
        count[chr(i)] = 0
    for i in range(0, len(wordlist)):       #wordlistから各アルファベットで始まる単語がいくつあるかを調べる
        for key in (wordlist[i])[:1]:
            if key in count:
                count[key] += 1

    return(count)

def start_end_check(pairlist):
    count = {}
    for key in pairlist:        #最初の文字、最後の文字のペアがいくつあるかを調べる
        if key in count:
            count[key] += 1
        else:
            count[key] = 1
    return(count)

def print_result(uselist, lowerlist):
    result_idx = []
    for i in range(0, len(shiritorilist)):
        result_idx.append(lowerlist.index(shiritorilist[i]))
    
    for i in result_idx:
        if(i == result_idx[-1]):
            print(uselist[i])
        else:
            print(uselist[i] + ' -> ', end = '')

def shiritori(wordlist, pair, count, s):
    next = []
    nextword = ''       #次の単語nextword
    count[s] -= 1       #count_dict更新

    for i in range(0, len(wordlist)):       #次の単語候補を探す
        if((wordlist[i])[:1] == s):
            next.append(wordlist[i])
    print(next)

    if(next == []):         #次の単語候補がない→終了
        return
    
    elif(len(next) == 1):         #次の単語候補が1つならそれを選ぶ
        nextword = next[0]   

    else:         #次の単語候補が2つ以上のとき
        for i in range(0, len(next)):
            if((count.get((next[i])[-1:]) == 0)):      #次の単語候補の中で、最後の文字を頭文字とする単語がない→それを選んで終わり
                nextword = next[i]
                shiritorilist.append(nextword) 
                return

        min_val = min(count.values())       #count_dictの値の最小値min_val
        k = 0
        while(nextword == ''):
            keys_of_min_val = [key for key in count if count[key] == (min_val + k)]         #値が(min_val + k)のときのキーkeys_of_min_val（どのアルファベットを頭文字とする単語が少ないか）
            print(keys_of_min_val)
            if(keys_of_min_val == []):
                k += 1
                continue

            for i in range(0, len(next)):
                for j in range(0, len(keys_of_min_val)):
                    if((next[i])[-1:] == keys_of_min_val[j]):       #単語候補の中の最後の文字とkeys_of_min_valが一致→その単語を選択
                        nextword = next[i]
                        break
                else:
                    continue
                break

            if(nextword != ''):         #ここまでで次の単語が決定していればbreak
                break
            else:
                for i in range(0, len(next)):
                    for j in range(0, len(keys_of_min_val)):
                        if(pair.get((next[i])[-1:] + keys_of_min_val[j]) != None):      #単語候補の中の最後の文字とkeys_of_min_valが次のターンでつながる→その単語を選択
                            nextword = next[i]
                            break
                    else:
                        continue
                    break
            k += 1
    
    shiritorilist.append(nextword)      #結果に挿入
    wordlist.remove(nextword)       #wordlist更新
    pair[s + nextword[-1:]] -= 1        #pair_dict更新
    if(pair[s + nextword[-1:]]) == 0:
        del pair[s + nextword[-1:]]
    shiritori(wordlist, pair, count, nextword[-1:])     #次のターンへ

def main():
    uselist = import_data()
    wordlist = list(map(str.lower, uselist))        #大文字→小文字
    wordlist2 = wordlist.copy()
    startstr = input()   

    pairlist = pair(wordlist)       #最初・最後の文字だけ抜き出したリスト
    pair_dict = start_end_check(pairlist)       #最初・最後の文字のペアがいくつあるかをまとめた辞書
    count_dict = start_check(wordlist)      #wordlistの中の最初の文字の数をアルファベット別にまとめた辞書

    shiritori(wordlist, pair_dict, count_dict, startstr)
    print_result(uselist, wordlist2)

main()