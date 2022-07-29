from collections import deque
import math
import copy

def bfs(maze, X, Y, sx, sy):
    maze[sy][sx] = 0        #スタート位置は手数0
    for i in range(0, Y):
        for j in range(0, X):
            if(maze[i][j] == ' ' or maze[i][j] == 'g'):         #進める位置は手数を無限大にしておく
                maze[i][j] = math.inf

    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    que = deque([(sy, sx)])         #スタート位置の座標をキューに挿入

    while que:
        y, x = que.popleft()        #座標をキューから取り出す
        for i in range(0, 4):       #キューから取り出した座標の4近傍を探索
            x_next = x + dx[i]
            y_next = y + dy[i]
            if(0 <= x_next < X and 0 <= y_next < Y):
                if(maze[y_next][x_next] != 'X'):
                    dist = maze[y_next][x_next]
                    if(dist > maze[y][x] + 1):
                        maze[y_next][x_next] = maze[y][x] + 1       #手数を更新
                        que.append((y_next, x_next))        #キューに挿入

def route_find(maze, mazecopy, X, Y, gx, gy):
    short_route = maze[gy][gx]      #ゴールまでにかかる最短の手数short_route
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    x, y = gx, gy
    for i in range(short_route, 1, -1):     #ゴール位置から遡っていく
        for j in range(0, 4):
            x_next = x + dx[j]
            y_next = y + dy[j]
            if(0 <= x_next < X and 0 <= y_next < Y):
                if(maze[y_next][x_next] == i - 1):      #通った経路の座標のところを+にする
                    mazecopy[y_next][x_next] = '+'
                    x, y = x_next, y_next
                    break

def print_maze(mazecopy, X, Y):
    print('')
    print('---maze_result---')
    for i in range(0, Y):
        for j in range(0, X):
            print(mazecopy[i][j], end = '')
        print('')


def main():
    X, Y = (int(n) for n in input().split())        #列数Xと行数Yを標準入力から受け取る
    maze = []
    for i in range(0, Y):       #1行ごと迷路データを受け取る
        array = list(input())
        maze.append(array)
    
    SFlag = False
    GFlag = False
    for i in range(0, Y):
        for j in range(0, X):
            if(maze[i][j] == 's'):      #スタート位置の座標を探す
                sy, sx = i, j
                SFlag = True
            elif(maze[i][j] == 'g'):        #ゴール位置の座標を探す
                gy, gx = i, j
                GFlag = True
            
            if(SFlag == True and GFlag == True):        #スタート、ゴールの座標の両方見つかったらbreak
                break
        else:
            continue
        break

    mazecopy = copy.deepcopy(maze)          #迷路データをディープコピー
    bfs(maze, X, Y, sx, sy)
    route_find(maze, mazecopy, X, Y, gx, gy)

    '''
    print('')
    for i in range(0, Y):
        for j in range(0, X):
            s_rjust = str(maze[i][j]).rjust(3)
            print(s_rjust, end = '')
        print('')
    '''

    print_maze(mazecopy, X, Y)


if __name__ == "__main__":
    main()