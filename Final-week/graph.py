def graph_color(graph, color_no, result, node):
    if list(result.values()).count(0) == 0:
        return True

    for color in ['red', 'green', 'blue']:
        isColorValid = True
        for j in graph[node]:
            if result[j] == color:
                isColorValid = False

        if isColorValid:
            result[node] = color
            if graph_color(graph, color_no, result, next_node(graph, node)):
                return True

    return False        

def next_node(graph, current_node):
    nodes = list(graph.keys())
    index = nodes.index(current_node)
    next_index = (index + 1) % len(nodes)
    return nodes[next_index]

if __name__ == '__main__':    
    node_no = 4
    color_no = 3

    result = {"Dhaka":0, "Sylhet":0, "Rajshahi":0, "Chittagong":0}
    graph = { "Dhaka": ["Sylhet", "Rajshahi", "Chittagong"],
              "Sylhet": ["Dhaka", "Rajshahi"],
              "Rajshahi": ["Dhaka", "Sylhet", "Chittagong"],
              "Chittagong": ["Dhaka", "Rajshahi"] }

    isColoringPossible = graph_color(graph, color_no, result, "Dhaka")

    if isColoringPossible == True:
        for node, color in result.items():
            print(f"{node} is colored {color}")
    else:
        print("no solution exists...")