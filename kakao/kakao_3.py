class Food :
    def __init__ (self, time, num) :
        self.time = time
        self.num = num

def min_food (list_food_class) :
    min = list_food_class[0]
    for i in range (1, len (list_food_class)) :
        if min.time > list_food_class[i].time :
            min = list_food_class[i]
    return min

def sum_food (list_food_class) :
    sum = 0
    for i in range (len (list_food_class)) :
        sum += list_food_class[i].time

    return sum

def print_food (list_food_class, count) :
    result = str (count) + " ["
    for i in list_food_class :
        result += str (i.time) + " ,"
    result += "]"
    print (result)

def solution(food_times, k):
    list_food = food_times.copy()
    temp = k
    list_food_class = list ()
    list_food_time = list ()
    for i in range (len(food_times)) :
        list_food_class.append (Food(list_food[i], i + 1))

    if sum(list_food) < k :
        return -1

    count_zero =  1
    while (count_zero != 0) :
        # print_food (list_food_class, 0)
        # print (temp)
        min_food_class = min_food (list_food_class)
        min_food_time = min_food_class.time
        count_zero = 0
        if int (temp / len (list_food_class)) >= min_food_time :
            # print ("111111111111")
            for i in list_food_class :
                i.time -= min_food_time
                if i.time == 0 :
                    list_food_class.remove(i)
                    count_zero += 1
            temp = temp - min_food_time * (len(list_food_class) + count_zero)
        else :
            # print ("222222222222222")
            for i in list_food_class :
                i.time -= int (temp / len (list_food_class))
            temp = temp - int (temp / len(list_food_class)) * len (list_food_class)
            break

    # print_food (list_food_class, 0)
    # print (temp)
    count  = 0
    index = 0

    if sum_food (list_food_class) <= temp:
        return -1

    while True :
        # print_food (list_food_class, count)
        # print (index)
        # print (temp)
        if count == temp :
            if list_food_class[index].time != 0 :
                break
            else :
                index += 1
                if index == len (list_food_class) :
                    index = 0
                continue

        if list_food_class[index].time != 0 :
            list_food_class[index].time -= 1
            index += 1
            count += 1
        else :
            index += 1

        if index == len (list_food_class) :
            index = 0

    return list_food_class[index].num

food_times = [1, 1, 1]
k = 5
temp = solution (food_times, k)
print (temp)
