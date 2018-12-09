def solution(m, n, board):
    list_board = []

    answer = 0

    for i in range(m):
        list_temp = []
        for j in range(n):
            list_temp.append(board[i][j])
        list_board.append(list_temp)
    while True:
        list_remove = []
        for i in range(m - 1):
            for j in range(n - 1):
                if list_board[i][j] == list_board[i + 1][j] == list_board[i][j + 1] == list_board[i + 1][j + 1] != 'O':
                    list_remove.append((i, j))
                    list_remove.append((i + 1, j))
                    list_remove.append((i, j + 1))
                    list_remove.append((i + 1, j + 1))
        for i, j in list_remove:
            if list_board[i][j] != 'O':
                list_board[i][j] = 'O'
                answer += 1

        for i in range(2, m + 1):
            for j in range(n):
                if list_board[m - i][j] != 'O' and list_board[m - i + 1][j] == 'O':
                    a = m - i
                    while True :

                        if a == m - 1 :
                            break
                        if list_board[a + 1][j] != 'O' :
                            break
                        list_board[a + 1][j] = list_board[a][j]
                        list_board[a][j] = 'O'
                        a += 1

        for i in list_board :
            print (i)
        print ()
        if len(list_remove) == 0:
            break

    return answer


board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print (solution (4, 5, board))