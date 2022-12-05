# link: https://school.programmers.co.kr/learn/courses/30/lessons/81301
# solving method: string methods

def solution(s):
    Neo = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    Prodo = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    for i in range(0, 10):
        s = s.replace(Neo[i],Prodo[i])
    
    return int(s)
