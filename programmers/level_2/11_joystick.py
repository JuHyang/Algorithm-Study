def solution(name):
    capital = ["A", "B", "C", "D", "E", "F", "G", "H","I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U","V", "W", "X", "Y", "Z"]
    answer = 0
    status = 0
    for i in range (len (name)) :
        if status == 0:
            if name[i] == 'A' :
                status = 1
                continue
        elif status == 1 :
            if name[i] != 'A' :
                status = 2
            else :
                continue

        if capital.index(name[i]) < len (capital) / 2 :
            answer += capital.index(name[i])
        else :
            answer += len(capital) - capital.index(name[i])
    return answer


name ="AAAAABAAAAAAAA" ## 문제점
name = "AAAAAAAA"
print (solution (name))
