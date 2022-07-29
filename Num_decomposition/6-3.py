import copy
import sys

def preparation_data():
    data = list(input())        #189文字の数字列をリストで受け取る
    return data

def division(n, data, divided_list):
    if(len(divided_list) == 99):        #divided_listの長さが99なら終了
        for i in range(0, len(divided_list)):
            divided_list[i] = int(divided_list[i])
        print(divided_list)
        sys.exit()

    else:
        next_str1 = data[n]         #次の1文字を見る場合
        next_str2 = (data[n] + data[n + 1])         #次の2文字を見る場合
        
        next_list1 = copy.deepcopy(divided_list)        
        next_list1.append(data[n])          #次の1文字を追加したリストnext_list1

        if(n == 188):         #最後の文字なら1文字だけ読む
            if(next_str1 not in divided_list):
                division(n + 1, data, next_list1)
        
        next_list2 = copy.deepcopy(divided_list)        
        next_list2.append(data[n] + data[n + 1])        #次の2文字を追加したリストnext_list2
        
        if(n == 187):       #残り2文字の場合
            if(data[n + 1] == '0'):       #1文字先が0なら2文字（最後まで）読む
                if(next_str2 not in divided_list):
                    division(n + 2, data, next_list2)
            else:
                if(next_str1 not in divided_list):
                    division(n + 1, data, next_list1)
                
                if(next_str2 not in divided_list):
                    division(n + 2, data, next_list2)

        else:           #それ以外の場合
            if(data[n + 2] == '0'):         #2文字先が0なら1文字だけ読む
                if(next_str1 not in divided_list):
                    division(n + 1, data, next_list1)
        
            elif(data[n + 1] == '0'):       #1文字先が0なら2文字読む
                if(next_str2 not in divided_list):
                    division(n + 2, data, next_list2)
            
            else:
                if(next_str2 not in divided_list):
                    division(n + 2, data, next_list2)

                if(next_str1 not in divided_list):
                    division(n + 1, data, next_list1)            

def main():
    data = preparation_data()
    division(0, data, [])

if __name__ == "__main__":
    main()