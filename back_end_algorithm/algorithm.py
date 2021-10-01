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
# [30][][][] = Road
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

# ====================================
tuple([0,0,0,0]) = "DaeYangAI_1floor_gate_1"
tuple([0,0,0,0]) = "DaeYangAI_1floor_gate_1"
tuple([0,0,0,0]) = "DaeYangAI_1floor_gate_1"
tuple([0,0,0,0]) = "DaeYangAI_1floor_gate_1"
tuple([0,0,0,0]) = "DaeYangAI_1floor_gate_1"
tuple([0,0,0,0]) = "DaeYangAI_1floor_gate_1"
tuple([0,0,0,0]) = "DaeYangAI_1floor_gate_1"
tuple([0,0,0,0]) = "DaeYangAI_1floor_gate_1"
tuple([1,0,0,0]) = "Chungmu_1floor_gate_1"
tuple([1,0,0,0]) = "Chungmu_1floor_gate_1"
tuple([1,0,0,0]) = "Chungmu_1floor_gate_1"
tuple([1,0,0,0]) = "Chungmu_1floor_gate_1"
tuple([1,0,0,0]) = "Chungmu_1floor_gate_1"
tuple([1,0,0,0]) = "Chungmu_1floor_gate_1"
tuple([1,0,0,0]) = "Chungmu_1floor_gate_1"
tuple([1,0,0,0]) = "Chungmu_1floor_gate_1"
tuple([2,0,0,0]) = "StudentHall_1floor_gate_1"
tuple([2,0,0,1]) = "StudentHall_1floor_gate_2"



# 초기화 
def init(): 
    global graph, infinity, costs, parents, processed 
    graph = {} # 간선 정보 입력 
    graph[["DaeYang"]["First"]["kind"]["num"]] = {}
    graph["DaeYang"]["First"]["kind"]["num"]["end_point"] = 10

    graph["A"] = {} 
    graph["A"]["B"] = 5 
    graph["A"]["C"] = 0 
    graph["B"] = {} 
    graph["B"]["D"] = 15 
    graph["B"]["E"] = 20 
    graph["C"] = {} 
    graph["C"]["D"] = 30 
    graph["C"]["E"] = 35 
    graph["D"] = {}
    graph["D"]["F"] = 20 
    graph["E"] = {} 
    graph["E"]["F"] = 10 
    graph["F"] = {} 
    # ---------------------------------------- 
    infinity = float("inf") 
    # ------------------------------------------ 
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
    # ------------------------------------------- 
    processed = []


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


graph = {} # 간선 정보 입력 
graph[tuple([0,0,0,0])] = {}
graph[tuple([0,0,0,0])]["end_point"] = 10

print(graph)