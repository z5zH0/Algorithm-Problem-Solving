def solution(name):
    answer = 0
    check = []
    for i in name:
        if ord(i) > 78:
            check.append(ord('Z') - ord(i) + 1)
        else:
            check.append(ord(i) - ord('A'))
            
    idx = 0
    
    while True:
        answer += check[idx]
        check[idx] = 0
        
        if sum(check) == 0:
            break
            
        right = 1
        left = 1
        
        while check[idx + right] == 0:
            right += 1
            
        while check[idx - left] == 0:
            left += 1
        
        if right <= left:
            idx += right
            answer += right
        else:
            idx -= left
            answer += left
        
    return answer
