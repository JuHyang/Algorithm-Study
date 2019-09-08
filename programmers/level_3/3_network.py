

def solution(n, computers):
    answer = 0
    dict_computer = dict ()
    for i in range (n) :
        dict_computer[i] = []
        for j in range  (n) :
            if i != j :
                if computers[i][j] == 1 :
                    if i in dict_computer :
                        dict_computer[i].append(j)

    queue = []
    visited = []

    index = 0
    while len (dict_computer) != 0 :
        if index in visited :
            for i in dict_computer :
                index = i
                break
            continue
        
        visited.append(index)
        if len (dict_computer[index]) == 0:
            answer += 1
            del dict_computer[index]
            continue

        for i in dict_computer[index] :
            if i not in visited :
                queue.append(i)

        del dict_computer[index]
        if len(queue) == 0 :
            answer += 1
            for i in dict_computer :
                index = i
                break
            continue
        index = queue.pop(0)
        
    return answer