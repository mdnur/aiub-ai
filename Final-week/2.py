def graph_color(graph, color_no, result, node):
    if list(result.values()).count(0) == 0:
        return True

    for color in range(1, color_no + 1):
        isColorValid = True
        for j in range(1, len(graph) + 1):
            if j in graph[node] and result[j] == color:
                isColorValid = False

        if isColorValid:
            result[node] = color
            if graph_color(graph, color_no, result, node + 1):
                return True

    return False


if __name__ == '__main__':
    node_names = {'Dhaka': 1, 'Sylhet': 2, 'Rajshahi': 3, 'Chitagong': 4}
    color_names = {1: 'red', 2: 'blue', 3: 'green'}

    node_no = len(node_names)
    color_no = len(color_names)

    result = {1: 0, 2: 0, 3: 0, 4: 0}

    graph = {'Dhaka': ['Sylhet', 'Rajshahi', 'Chitagong'],
             'Sylhet': ['Dhaka', 'Rajshahi'],
             'Rajshahi': ['Dhaka', 'Sylhet', 'Chitagong'],
             'Chitagong': ['Dhaka', 'Rajshahi']}

    isColoringPossible = graph_color(graph, color_no, result, 1)

    if isColoringPossible:
        result_names = {node_names[name]: color_names[color] for name, color in result.items()}
        print(result_names)
    else:
        print("No solution exists.")