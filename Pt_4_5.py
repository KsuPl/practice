def find_rouds(my_dict, start, end, way):
    lstways = []
    way = way + [start]
    if start == end:
        return [way]
    for item in my_dict[start]:
        ways = find_rouds(my_dict, item, end, way)
        lstways.extend(ways)
    return lstways


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
first = 'A'
final = 'F'
way1 = []
print('Все пути из вершины ' + first + ' до вершины ' + final + ':', *find_rouds(graph, first, final, way1))
