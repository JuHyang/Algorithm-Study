def DFS (node_dict, marked, V) :
    temp_marked = marked.copy()
    temp_dict = node_dict.copy()

    stack = [V]
    temp_marked[V] = True
    while True :
        now = stack[-1]
        stack.append(temp_marked[now][0])


    return;
input_str = input ()

list_input = input_str.split()

N = int (list_input[0])
M = int (list_input[1])
V = int (list_input[2])

node_dict = dict()
marked = [True]

for i in range (M) :
    marked.append(False)
    input_str = input ()
    list_input = input_str.split()

    node = int (list_input[0])
    nextNode = int (list_input[1])

    if node not in node_dict :
        node_dict[node] = list ()

    node_dict[node].append(nextNode)
    node_dict[node].sort()

print (node_dict)

DFS (node_dict, marked, V)
