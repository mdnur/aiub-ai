def graph_color(graph, color_no, result, node):
    if list(result.values()).count(0) == 0:
        return True

    for color in range(1, color_no + 1):
        is_color_valid = True
        for j in range(1, len(graph) + 1):
            if j in graph[node] and result[j] == color:
                is_color_valid = False

        if is_color_valid:
            result[node] = color
            if graph_color(graph, color_no, result, node + 1):
                return True

    return False


if __name__ == '__main__':
    node_no = 4
    color_no = 3

    # colors = [0, 0, 0, 0]
    result = {1: 0, 2: 0, 3: 0, 4: 0}

    graph = {1: [2, 3, 4],
             2: [1, 3],
             3: [1, 2, 4],
             4: [1, 3]}

    isColoringPossible = graph_color(graph, color_no, result, 1)

    if isColoringPossible:
        print(result)
    else:
        print("no solution exists...")
