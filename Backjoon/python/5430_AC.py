T = int (input ())
for i in range (T) :
    status = 0
    p = input ()
    n = int (input ())
    arr = input ()
    arr = arr[1:-1]
    list_num = arr.split(",")
    if arr == '' :
        list_num = []
    for j in range (n) :
        list_num[j] = int (list_num[j])
    for j in p :
        if j == "R" :
            list_num.reverse()
        elif j == "D" :
            if len(list_num) == 0 :
                print ("error")
                status = 1
                break
            else :
                list_num.pop(0)
    if status != 1 :
        result = "["
        for i in range (len (list_num)) :
            if i == len (list_num) - 1 :
                result += str (list_num[i])
            else :
                result += str (list_num[i]) + ","
        result += "]"
        print (result)
