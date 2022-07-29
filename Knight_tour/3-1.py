def print_board(n, board):          #盤面を表示する関数
    for i in range(0, n):
        for j in range(0, n):
            print('+----', end = '')
        print('+')
        for j in range(0, n):
            print('|', end = '')
            for k in range(0, 4 - len(str(board[i][j]))):
                print(' ', end = '')
            print(board[i][j], end = '')
        print('|')
    for i in range(0, n):
        print('+----', end = '')
    print('+')

def knight_tour(board, count, x, y, n):         #ナイトツアーを実行する関数（盤面、手数、x座標、y座標、nを受け取り、flagを返す）
    dx = [2, 2, 1, -1, -2, -2, -1, 1]       #横方向に動ける場所
    dy = [1, -1, -2, -2, -1, 1, 2, 2]       #縦方向に動ける場所

    for i in range(0, 8):           #動ける場所は計8箇所なので8回ループ
        check_x = x + dx[i]         #次のx座標候補
        check_y = y + dy[i]         #次のy座標候補
        flag = 0        #flagは0（失敗）でスタート
        if(0 <= check_x < n and 0 <= check_y < n and board[check_x][check_y] == 0):         
            board[check_x][check_y] = count         #とりあえず手数を盤面に代入
            #print_board(n, board)
            if(count < n * n):          
                flag = knight_tour(board, count + 1, check_x, check_y, n)           #最後まで探索されていない場合、次の手以降を実行
                if(flag == 0):
                    board[check_x][check_y] = 0         #次手以降でflagが0だったら失敗なので0に戻す
            else:
                flag = 1        #最後まで探索されていればflagを1にする
        if(flag == 1):
            break       #flagが1ならすでに成功しているのでループを抜ける
        
    return(flag)


def main():
    n = int(input('n = '))
    board = [[0 for i in range(n)] for j in range(n)]
    board[n - 1][n - 1] = 1         #初期位置が1
    
    if(knight_tour(board, 2, n - 1, n - 1, n) == 1):        #ナイトツアー実行（返り値1なら成功→盤面を表示）
        print_board(n, board)
    
    else:
        print('解なし')

main()