def BFS (target, i, numbers, stack, result) :
    print ("i : ", i)
    print ("stack : ", stack)
    print ("result : ", result)
    if i == len (numbers) - 1 :
        if stack + numbers[i] == target :
            result += 1
        if stack - numbers[i] == target :
            result += 1
        print (result)
        return result
    result = BFS (target, i + 1, numbers, stack + numbers[i], result)
    print (result)
    result = BFS (target, i + 1, numbers, stack - numbers[i], result)
    print (result)

    return result

def solution(numbers, target):

    answer = BFS (target, 0, numbers, 0, 0)

    return answer


numbers= [1,1,1,1,1]
target = 3


solution (numbers, 3)