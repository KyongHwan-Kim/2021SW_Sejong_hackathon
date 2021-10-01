import heapq
grep_tuple = tuple('&')
graph = {}

working_speed = 1.38 #(m/s)

running_speed = 2.5 #(m/s)
#==========Main_Gate=============[building][floor][kind][Kind_number][gate_number]
graph[str([4,0,0,0])] = {} #"MainGate_1"
graph[str([4,0,0,0])][str([4,0,0,1])] = 15.67
graph[str([4,0,0,0])][str([30,0,0,0])] = 29.75
graph[str([4,0,0,1])] = {}
graph[str([4,0,0,1])][str([30,0,0,0])] = 32.79

#===========Road_str=============[building][floor][kind][Kind_number][gate_number]
graph[str([30,0,0,0])] = {} #"Road_str1_node1"
graph[str([30,0,0,0])][str([30,0,0,1])] = 14
graph[str([30,0,0,0])][str([2,0,0,0])] = 4
graph[str([30,0,0,0])][str([2,0,1,0])] = 4
graph[str([30,0,0,0])][str([30,5,0,0])] = 4

graph[str([30,0,0,1])] = {} #"Road_str1_node2
graph[str([30,0,0,1])][str([30,1,0,0])] = 7
graph[str([30,0,0,1])][str([30,2,0,0])] = 7


graph[str([30,1,0,0])] = {} #"Road_str2_node1
graph[str([30,1,0,0])][str([30,1,0,1])] = 9
graph[str([30,1,0,0])][str([30,5,0,7])] = 9
graph[str([30,1,0,0])][str([30,5,0,2])] = 9
graph[str([30,1,0,0])][str([30,2,0,1])] = 9

graph[str([30,1,0,1])] = {} #"Road_str2_node2
graph[str([30,1,0,1])][str([30,2,0,2])] = 9
graph[str([30,1,0,1])][str([30,3,0,0])] = 9
graph[str([30,1,0,1])][str([30,3,0,1])] = 9

graph[str([30,2,0,0])] = {} #"Road_str3_node1
graph[str([30,2,0,0])][str([30,2,0,1])] = 15
graph[str([30,2,0,1])] = {} #"Road_str3_node2
graph[str([30,2,0,1])][str([1,0,0,0])] = 13
graph[str([30,2,0,1])][str([30,2,0,2])] = 13
graph[str([30,2,0,2])] = {} #"Road_str3_node3
graph[str([30,2,0,2])][str([1,0,0,1])] = 13

graph[str([30,3,0,0])] = {}
graph[str([30,3,0,0])][str([30,3,0,2])] = 14
graph[str([30,3,0,1])] = {}
graph[str([30,3,0,1])][str([30,3,0,2])] = 14
graph[str([30,3,0,2])] = {}
graph[str([30,3,0,2])][str([30,3,0,3])] = 14
graph[str([30,3,0,3])] = {}
graph[str([30,3,0,3])][str([30,3,0,4])] = 14
graph[str([30,3,0,3])][str([30,3,0,5])] = 14
graph[str([30,3,0,4])] = {}
graph[str([30,3,0,4])][str([30,3,0,7])] = 14
graph[str([30,3,0,5])] = {}
graph[str([30,3,0,5])][str([30,3,0,6])] = 14
graph[str([30,3,0,6])] = {}
graph[str([30,3,0,6])][str([30,3,0,8])] = 14
graph[str([30,3,0,6])][str([30,3,0,7])] = 14
graph[str([30,3,0,7])] = {}
graph[str([30,3,0,7])][str([0,0,0,0])] = 14
graph[str([30,3,0,7])][str([30,5,0,4])] = 14
graph[str([30,3,0,7])][str([2,-1,0,1])] = 14
graph[str([30,3,0,8])] = {}
graph[str([30,3,0,8])][str([30,3,0,7])] = 14

graph[str([30,5,0,0])] = {}
graph[str([30,5,0,0])][str([30,5,0,1])] = 123
graph[str([30,5,0,1])] = {}
graph[str([30,5,0,1])][str([30,5,0,2])] = 123
graph[str([30,5,0,2])] = {}
graph[str([30,5,0,2])][str([30,5,0,8])] = 123
graph[str([30,5,0,2])][str([30,5,0,3])] = 123
graph[str([30,5,0,2])][str([30,5,0,7])] = 123
graph[str([30,5,0,3])] = {}
graph[str([30,5,0,3])][str([30,5,0,5])] = 213
graph[str([30,5,0,3])][str([30,5,0,4])] = 5234
graph[str([30,5,0,4])] = {}
graph[str([30,5,0,5])] = {}
graph[str([30,5,0,5])][str([30,5,0,6])] = 54
graph[str([30,5,0,6])] = {}
graph[str([30,5,0,6])][str([3,0,0,1])] = 54
graph[str([30,5,0,6])][str([30,3,0,2])] = 54
graph[str([30,5,0,7])] = {}
graph[str([30,5,0,7])][str([30,3,0,0])] = 213
graph[str([30,5,0,7])][str([3,0,0,0])] = 213
graph[str([30,5,0,8])] = {}
graph[str([30,5,0,8])][str([30,5,0,3])] = 123
graph[str([30,5,0,8])][str([2,-1,0,0])] = 123

graph[str([31,0,0,0])] = {}
graph[str([31,0,0,0])][str([31,0,0,1])] = 123
graph[str([31,0,0,0])][str([0,0,0,1])] = 123
graph[str([31,0,0,1])] = {}
graph[str([31,0,0,1])][str([31,0,0,2])] = 123
graph[str([31,0,0,1])][str([30,3,0,7])] = 12323
graph[str([31,0,0,2])] = {}
graph[str([31,0,0,2])][str([4,0,0,0])] = 123
graph[str([31,0,0,2])][str([2,0,0,1])] = 123

#===========StudentHall===========[building][floor][kind][Kind_number][gate_number]
#Gate
graph[str([2,0,0,0])] = {} # gate_1
graph[str([2,0,0,1])] = {} # gate_2
graph[str([2,-1,0,0])] = {} # B1 gate_2
graph[str([2,-1,0,1])] = {} # B1 gate_3
graph[str([2,0,0,2])] = {} #"StudentHall_1floor_gate_3"
#Shop
graph[str([2,0,1,0])] = {} #ParisBagate


#===========DaeYangAI===========[building][floor][kind][Kind_number][gate_number]
graph[str([0,0,0,0])] = {} #"DaeYangAI_1floor_gate_1"
graph[str([0,0,0,1])] = {} #"DaeYangAI_1floor_gate_2"
graph[str([0,0,0,2])] = {} #"DaeYangAI_1floor_gate_3"

#=============Gunja=============[building][floor][kind][Kind_number][gate_number]
graph[str([1,0,0,0])] = {} #"Gunja_1floor_gate_1"
graph[str([1,0,0,1])] = {} #"Gunja_1floor_gate_2"
graph[str([1,0,0,0])][str([1,0,0,0])] = 23

#==========Sejong_gaun==========[building][floor][kind][Kind_number][gate_number]
graph[str([3,0,0,0])] = {} # sejong_1floor_gate_1"
graph[str([3,0,0,1])] = {} # sejong_1floor_gate_2"

def dijkstra_one(graph, start, end):
    distances = {vertex: [float('inf'), start] for vertex in graph}

    distances[start] = [0, start]

    queue = []

    heapq.heappush(queue, [distances[start][0], start])

    while queue:
        current_distance, currnet_vertex = heapq.heappop(queue)
        if distances[currnet_vertex][0] < current_distance:
            continue
        for adjacent, weight in graph[currnet_vertex].items():
            distance = current_distance + weight

            if distance < distances[adjacent][0]:
                distances[adjacent] = [distance, currnet_vertex]
                heapq.heappush(queue, [distance, adjacent])

    path = end
    path_output = end + '->'
    while distances[path][1] != start:
        path_output += distances[path][1] + '->'
        path = distances[path][1]
    path_output += start
    return distance

total_distance = dijkstra_one(graph, str([4,0,0,0]), str([30,2,0,1]))
print('total distance : '+ str(dijkstra_one(graph, str([4,0,0,0]), str([30,2,0,1])))+'m')

print('predict working time : '+str((total_distance/working_speed)/60))
print('predict running time : '+str((total_distance/running_speed)/60))