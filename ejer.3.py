import heapq

class Graph:
    def __init__(self):
        self.edges = {}
    
    def add_vertex(self, vertex, vertex_type):
        self.edges[vertex] = {"type": vertex_type, "connections": {}}
    
    def connect_vertices(self, vertex1, vertex2, weight):
        self.edges[vertex1]["connections"][vertex2] = weight
        self.edges[vertex2]["connections"][vertex1] = weight
    
    def dijkstra(self, start, end):
        shortest_paths = {start: (None, 0)}
        current_vertex = start
        visited = set()
        
        while current_vertex != end:
            visited.add(current_vertex)
            destinations = self.edges[current_vertex]["connections"]
            weight_to_current_vertex = shortest_paths[current_vertex][1]

            for next_vertex, weight in destinations.items():
                new_weight = weight_to_current_vertex + weight
                if next_vertex not in shortest_paths:
                    shortest_paths[next_vertex] = (current_vertex, new_weight)
                else:
                    current_shortest_weight = shortest_paths[next_vertex][1]
                    if current_shortest_weight > new_weight:
                        shortest_paths[next_vertex] = (current_vertex, new_weight)
            
            next_destinations = {vertex: weight for vertex, weight in shortest_paths.items() if vertex not in visited}
            if not next_destinations:
                return None
            current_vertex, weight = sorted(next_destinations.items(), key=lambda x: x[1][1])[0]

        path = []
        while current_vertex is not None:
            path.append(current_vertex)
            next_vertex = shortest_paths[current_vertex][0]
            current_vertex = next_vertex
        path = path[::-1]

        return path, shortest_paths[end][1]

# Crear la red de ferrocarriles
railroad_network = Graph()

# Añadir estaciones
stations = ["King's Cross", "Waterloo", "Victoria Train Station", "Liverpool Street Station", "St. Pancras"]
for station in stations:
    railroad_network.add_vertex(station, "station")

# Añadir desvíos
for i in range(1, 13):
    railroad_network.add_vertex(str(i), "switch")

# Conectar estaciones y desvíos siguiendo las restricciones
railroad_network.connect_vertices("King's Cross", "1", 5)
railroad_network.connect_vertices("1", "2", 7)
railroad_network.connect_vertices("2", "Waterloo", 4)

railroad_network.connect_vertices("Victoria Train Station", "3", 4)
railroad_network.connect_vertices("3", "4", 6)
railroad_network.connect_vertices("4", "Liverpool Street Station", 5)

railroad_network.connect_vertices("St. Pancras", "5", 2)
railroad_network.connect_vertices("5", "6", 3)
railroad_network.connect_vertices("6", "King's Cross", 5)

# Encontrar el camino más corto entre las estaciones
path1, distance1 = railroad_network.dijkstra("King's Cross", "Waterloo")
path2, distance2 = railroad_network.dijkstra("Victoria Train Station", "Liverpool Street Station")
path3, distance3 = railroad_network.dijkstra("St. Pancras", "King's Cross")

print(f"Camino más corto desde King's Cross a Waterloo: {distance1}")
print(f"Camino más corto desde Victoria Train Station a Liverpool Street Station: {distance2}")
print(f"Camino más corto desde St. Pancras a King's Cross: {distance3}")
