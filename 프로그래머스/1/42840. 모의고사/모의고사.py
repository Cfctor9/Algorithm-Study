def solution(answers):
    answer = []
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    
    fir = 0
    sec = 0
    trd = 0
    
    for i in range(len(answers)):
        if answers[i] == first[i%5]:
            fir = fir + 1
        if answers[i] == second[i%8]:
            sec = sec + 1
        if answers[i] == third[i%10]:
            trd = trd + 1
    
    max_score = max(fir,sec,trd)
    ans_list = []
    ans_list.append(fir)
    ans_list.append(sec)
    ans_list.append(trd)
    
    if max_score ==  fir:
        answer.append(1)
    if max_score == sec:
        answer.append(2)
    if max_score == trd:
        answer.append(3)
            
        
            
    return answer