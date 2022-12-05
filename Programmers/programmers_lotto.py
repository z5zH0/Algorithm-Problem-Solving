def solution(lottos, win_nums):
    answer = []
    minimum = 0
    for i in lottos:
        for j in range (0, len(win_nums)):
            if i == win_nums[j]:
                minimum += 1
    maximum = minimum + lottos.count(0)
    
    answer.append(maximum)
    answer.append(minimum)
    
    for i in range (0, len(answer)):
        if answer[i] == 6:
            answer[i] = 1
        elif answer[i] == 5:
            answer[i] = 2
        elif answer[i] == 4:
            answer[i] = 3
        elif answer[i] == 3:
            answer[i] = 4
        elif answer[i] == 2:
            answer[i] = 5
        else:
            answer[i] = 6
    
    return answer
