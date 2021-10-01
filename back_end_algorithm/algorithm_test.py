import heapq
grep_tuple = tuple('&')
graph = {}

working_speed = 1.38 #(m/s)

running_speed = 2.5 #(m/s)
#==========Main_Gate=============[building][floor][kind][Kind_number][gate_number]
graph[str([4,0,0,0])] = {} #"MainGate_1"
graph[str([4,0,0,0])][str([4,0,0,1])] = 15.67
graph[str([4,0,0,0])][str([31,0,0,2])] = 15.67
graph[str([4,0,0,0])][str([30,0,0,0])] = 29.75
graph[str([4,0,0,1])] = {}
graph[str([4,0,0,1])][str([30,0,0,0])] = 32.79
graph[str([4,0,0,1])][str([4,0,0,0])] = 32.79

#===========Road_str=============[building][floor][kind][Kind_number][gate_number]
graph[str([30,0,0,0])] = {} #"Road_str1_node1"
graph[str([30,0,0,0])][str([30,0,0,1])] = 43.92
graph[str([30,0,0,0])][str([2,0,0,0])] = 16.54
graph[str([30,0,0,0])][str([2,0,3,0])] = 19.52
graph[str([30,0,0,0])][str([30,5,0,0])] = 19.88

graph[str([30,0,0,1])] = {} #"Road_str1_node2
graph[str([30,0,0,1])][str([30,1,0,0])] = 50.06
graph[str([30,0,0,1])][str([30,2,0,0])] = 30.67


graph[str([30,1,0,0])] = {} #"Road_str2_node1
graph[str([30,1,0,0])][str([30,1,0,1])] = 37.15
graph[str([30,1,0,0])][str([30,5,0,7])] = 15.68
graph[str([30,1,0,0])][str([30,5,0,2])] = 31.66
graph[str([30,1,0,0])][str([30,2,0,1])] = 17.17

graph[str([30,1,0,1])] = {} #"Road_str2_node2
graph[str([30,1,0,1])][str([30,2,0,2])] = 12.45
graph[str([30,1,0,1])][str([30,3,0,0])] = 18.05
graph[str([30,1,0,1])][str([30,3,0,1])] = 18.21

graph[str([30,2,0,0])] = {} #"Road_str3_node1
graph[str([30,2,0,0])][str([30,2,0,1])] = 39.75
graph[str([30,2,0,1])] = {} #"Road_str3_node2
graph[str([30,2,0,1])][str([1,0,0,0])] = 8.19
graph[str([30,2,0,1])][str([30,2,0,2])] = 26.52
graph[str([30,2,0,2])] = {} #"Road_str3_node3
graph[str([30,2,0,2])][str([1,0,0,1])] = 10.83

graph[str([30,3,0,0])] = {}
graph[str([30,3,0,0])][str([30,3,0,2])] = 17.85
graph[str([30,3,0,1])] = {}
graph[str([30,3,0,1])][str([30,3,0,2])] = 17.05
graph[str([30,3,0,2])] = {}
graph[str([30,3,0,2])][str([30,3,0,3])] = 13.76
graph[str([30,3,0,3])] = {}
graph[str([30,3,0,3])][str([30,3,0,4])] = 9.57
graph[str([30,3,0,3])][str([30,3,0,5])] = 30.17
graph[str([30,3,0,4])] = {}
graph[str([30,3,0,4])][str([30,3,0,7])] = 57.31
graph[str([30,3,0,5])] = {}
graph[str([30,3,0,5])][str([30,3,0,6])] = 5.52
graph[str([30,3,0,6])] = {}
graph[str([30,3,0,6])][str([30,3,0,8])] = 15.50
graph[str([30,3,0,6])][str([30,3,0,7])] = 29.73
graph[str([30,3,0,7])] = {}
graph[str([30,3,0,7])][str([0,0,0,0])] = 7.10
graph[str([30,3,0,7])][str([30,5,0,4])] = 64.97
graph[str([30,3,0,7])][str([2,-1,0,1])] = 71.91
graph[str([30,3,0,8])] = {}
graph[str([30,3,0,8])][str([30,3,0,7])] = 24.06

graph[str([30,5,0,0])] = {}
graph[str([30,5,0,0])][str([30,5,0,1])] = 23.34
graph[str([30,5,0,1])] = {}
graph[str([30,5,0,1])][str([30,5,0,2])] = 29.36
graph[str([30,5,0,2])] = {}
graph[str([30,5,0,2])][str([30,5,0,8])] = 23.8
graph[str([30,5,0,2])][str([30,5,0,3])] = 20.96
graph[str([30,5,0,2])][str([30,5,0,7])] = 29.30
graph[str([30,5,0,3])] = {}
graph[str([30,5,0,3])][str([30,5,0,5])] = 8.18
graph[str([30,5,0,3])][str([30,5,0,4])] = 36.34
graph[str([30,5,0,4])] = {}
graph[str([30,5,0,5])] = {}
graph[str([30,5,0,5])][str([30,5,0,6])] = 30.22
graph[str([30,5,0,6])] = {}
graph[str([30,5,0,6])][str([3,0,0,1])] = 2.87
graph[str([30,5,0,6])][str([30,3,0,2])] = 35.50
graph[str([30,5,0,7])] = {}
graph[str([30,5,0,7])][str([30,3,0,0])] = 28.24
graph[str([30,5,0,7])][str([3,0,0,0])] = 9.82
graph[str([30,5,0,8])] = {}
graph[str([30,5,0,8])][str([30,5,0,3])] = 19.44
graph[str([30,5,0,8])][str([2,-1,0,0])] = 12.59

graph[str([31,0,0,0])] = {}
graph[str([31,0,0,0])][str([31,0,0,1])] = 16.88
graph[str([31,0,0,0])][str([0,0,0,1])] = 32.94
graph[str([31,0,0,1])] = {}
graph[str([31,0,0,1])][str([31,0,0,2])] = 81.73
graph[str([31,0,0,1])][str([31,0,0,0])] = 81.73 # 추가
graph[str([31,0,0,1])][str([30,3,0,7])] = 67.61
graph[str([31,0,0,2])] = {}
graph[str([31,0,0,2])][str([4,0,0,0])] = 50.36
graph[str([31,0,0,2])][str([31,0,0,1])] = 50.36 # 추가
graph[str([31,0,0,2])][str([2,0,0,2])] = 12.47

#===========StudentHall===========[building][floor][kind][Kind_number][gate_number]
#Gate
graph[str([2,0,0,0])] = {} # gate_1
graph[str([2,0,0,1])] = {} # gate_2
graph[str([2,-1,0,0])] = {} # B1 gate_2
graph[str([2,-1,0,1])] = {} # B1 gate_3
graph[str([2,0,0,2])] = {} #"StudentHall_1floor_gate_3"
#Shop
graph[str([2,0,3,0])] = {} #ParisBagate


#===========DaeYangAI===========[building][floor][kind][Kind_number][gate_number]
graph[str([0,0,0,0])] = {} #"DaeYangAI_1floor_gate_1"
graph[str([0,0,0,1])] = {} #"DaeYangAI_1floor_gate_2"
graph[str([0,0,0,2])] = {} #"DaeYangAI_1floor_gate_3"

#=============Gunja=============[building][floor][kind][Kind_number][gate_number]
graph[str([1,0,0,0])] = {} #"Gunja_1floor_gate_1"
graph[str([1,0,0,1])] = {} #"Gunja_1floor_gate_2"

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
    print(path_output)
    return distance

total_distance = dijkstra_one(graph, str([4,0,0,1]), str([0,0,0,1]))
print('total distance : '+ str(total_distance)+'m')

print('predict working time : '+str((total_distance/working_speed)/60)+'min')
print('predict running time : '+str((total_distance/running_speed)/60)+'min')