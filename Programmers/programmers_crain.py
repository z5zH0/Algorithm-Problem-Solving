def solution(board, moves):
    basket = []
    pang = 0
    for i in range(len(moves)):
        for j in range(len(board)):
            curr = moves[i]-1
            if board[j][curr] == 0:
                continue
            if len(basket) > 0:
                if board[j][curr] == basket[-1]:
                    pang += 2
                    basket.pop()
                    board[j][curr] = 0
                    break
            basket.append(board[j][curr])
            board[j][curr] = 0
            break
            
    return pang
