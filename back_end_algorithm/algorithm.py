import queue

graph = {}
infinity = float("inf")
cost = {}
parents = {}
processed = []

# definition [building][floor][kind][Kind_number][gate_number]
# [0][][][] = DaeYangAI
# [1][][][] = Gunja
# [2][][][] = StudentHall
# [3][][][] = MainGate
# [30][][][] = Road
# [30][1][][]= street
# [30][1][0] = node num
# [][-2][][] = B1
# [][-1][][] = B2
# [][0][][] = 1F
# [][1][][] = 2F
# [][2][][] = 3F
# [][][0][] = Gate
# [][][1][] = Shop
# [][][2][] = classroom
# [][][3][] = EV Gate
# [][][4][] = Stair Gate

#==========Main_Gate=============[building][floor][kind][Kind_number][gate_number]
graph[tuple([3,0,0,0])] = {} #"MainGate_1"
graph[tuple([3,0,0,0])][tuple([3,0,0,1])] = 0
graph[tuple([3,0,0,0])][tuple([30,0,0,0])] = 0
graph[tuple([3,0,0,0])][tuple([3,0,0,1])] = 0

#===========Road_str=============[building][floor][kind][Kind_number][gate_number]
graph[tuple([30,0,0,0])] = {} #"Road_str1_node1"
graph[tuple([30,0,0,0])][tuple([3,0,0,1])] = 0
graph[tuple([0,0,0,0])] = {} 
graph[tuple([0,0,0,0])] = {} 
graph[tuple([0,0,0,0])] = {} 
graph[tuple([0,0,0,0])] = {} 

#===========StudentHall===========[building][floor][kind][Kind_number][gate_number]
#Gate
graph[tuple([2,0,0,0])] = {} # gate_1
graph[tuple([2,0,0,0])][tuple([30,0,0,0])] = 0
graph[tuple([2,0,0,1])] = {} # gate_2

graph[tuple([2,0,0,2])] = {} #"StudentHall_1floor_gate_3"
#Shop
graph[tuple([2,0,1,0])] = {} #ParisBagate
graph[tuple([2,0,1,0])][tuple([30,0,0,0])] = 0

#===========DaeYangAI===========[building][floor][kind][Kind_number][gate_number]
graph[tuple([0,0,0,0])] = {} #"DaeYangAI_1floor_gate_1"
graph[tuple([0,0,0,0])][tuple([3,0,0,1])] = 0

#=============Gunja=============[building][floor][kind][Kind_number][gate_number]
graph[tuple([1,0,0,0])] = {} #"Gunja_1floor_gate_1"
graph[tuple([1,0,0,0])][tuple([1,0,0,0])] = 0




costs = {} # 해당 노드 최단경로 입력 
costs["A"] = infinity 
costs["B"] = infinity 
costs["C"] = infinity 
costs["D"] = infinity 
costs["E"] = infinity 
costs["F"] = infinity 
# ------------------------------------------- 
# parents = {} # 추적 경로를 위해 부모 설정 
parents["B"] = None 
parents["C"] = None 
parents["D"] = None 
parents["E"] = None 
parents["F"] = None 




def find_lowest_cost_node(costs): 
    lowest_cost = float("inf") 
    lowest_cost_node = None
    for node in costs: 
        cost = costs[node] 
        if cost < lowest_cost and node not in processed: 
            lowest_cost = cost 
            lowest_cost_node = node 
    return lowest_cost_node

# 다익스트라 알고리즘 
def dijkstra(graph, start, final): 
    node = start 
    costs[start] = 0 
    while node is not None: 
        cost = costs[node] 
        neighbors = graph[node] 
        for n in neighbors.keys(): 
            new_cost = cost + neighbors[n] 
            if costs[n] > new_cost: # 현재 가지고있는 cost보다 new_cost가 더 최단거리라면 
                costs[n] = new_cost # 갱신 
                parents[n] = node 
                processed.append(node) 
                node = find_lowest_cost_node(costs) # 경로 추적 로직 
    trace = [] 
    current = final 
    while current != start: 
        trace.append(current) 
        current = parents[current] 
        trace.append(start) 
        trace.reverse() 
        print("=== Dijkstra ===") 
        print(start, "에서 ", final, "까지의 정보") 
        print("최단 거리 : ", costs[final]) 
        print("진행 과정 : ", processed) 
        print("경로 : ", trace)



print(graph)