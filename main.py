import networkx as nx
from networkx.algorithms.approximation import christofides

class City:
    def __init__(self, name):
        self.name = name
        self.cities = {}

    def add_city(self, city, distance):
        self.cities[city] = distance

    def get_direct_cities(self):
        return list(self.cities.keys())

    def get_distance(self, city):
        return self.cities.get(city, None)

    def __str__(self):
        cities_str = ", ".join(
            [f"{connected_city.name} ({distance} km)" for connected_city, distance in self.cities.items()]
        )
        return f"City: {self.name}\nDirect Cities: {cities_str}"

texas_cities_names = [
    "Houston", "Dallas", "Austin", "San Antonio", "Fort Worth",
    "El Paso", "Arlington", "Corpus Christi", "Plano", "Lubbock",
    "Laredo", "Irving", "Garland", "Frisco", "Amarillo",
    "Brownsville", "Grand Prairie", "McAllen", "Pasadena", "Mesquite"
]

real_distances = {
    ('Houston', 'Houston'): 0,
    ('Houston', 'Dallas'): 91,
    ('Houston', 'Austin'): 53,
    ('Houston', 'San Antonio'): 68,
    ('Houston', 'Fort Worth'): 1,
    ('Houston', 'El Paso'): 88,
    ('Houston', 'Arlington'): 99,
    ('Houston', 'Corpus Christi'): 70,
    ('Houston', 'Plano'): 95,
    ('Houston', 'Lubbock'): 14,
    ('Houston', 'Laredo'): 52,
    ('Houston', 'Irving'): 22,
    ('Houston', 'Garland'): 69,
    ('Houston', 'Frisco'): 83,
    ('Houston', 'Amarillo'): 68,
    ('Houston', 'Brownsville'): 33,
    ('Houston', 'Grand Prairie'): 82,
    ('Houston', 'McAllen'): 79,
    ('Houston', 'Pasadena'): 64,
    ('Houston', 'Mesquite'): 64,
    ('Dallas', 'Dallas'): 0,
    ('Dallas', 'Austin'): 79,
    ('Dallas', 'San Antonio'): 49,
    ('Dallas', 'Fort Worth'): 69,
    ('Dallas', 'El Paso'): 99,
    ('Dallas', 'Arlington'): 28,
    ('Dallas', 'Corpus Christi'): 100,
    ('Dallas', 'Plano'): 26,
    ('Dallas', 'Lubbock'): 98,
    ('Dallas', 'Laredo'): 39,
    ('Dallas', 'Irving'): 50,
    ('Dallas', 'Garland'): 56,
    ('Dallas', 'Frisco'): 24,
    ('Dallas', 'Amarillo'): 48,
    ('Dallas', 'Brownsville'): 46,
    ('Dallas', 'Grand Prairie'): 52,
    ('Dallas', 'McAllen'): 100,
    ('Dallas', 'Pasadena'): 29,
    ('Dallas', 'Mesquite'): 46,
    ('Austin', 'Austin'): 0,
    ('Austin', 'San Antonio'): 13,
    ('Austin', 'Fort Worth'): 93,
    ('Austin', 'El Paso'): 69,
    ('Austin', 'Arlington'): 26,
    ('Austin', 'Corpus Christi'): 25,
    ('Austin', 'Plano'): 33,
    ('Austin', 'Lubbock'): 2,
    ('Austin', 'Laredo'): 6,
    ('Austin', 'Irving'): 34,
    ('Austin', 'Garland'): 8,
    ('Austin', 'Frisco'): 27,
    ('Austin', 'Amarillo'): 84,
    ('Austin', 'Brownsville'): 12,
    ('Austin', 'Grand Prairie'): 96,
    ('Austin', 'McAllen'): 32,
    ('Austin', 'Pasadena'): 80,
    ('Austin', 'Mesquite'): 71,
    ('San Antonio', 'San Antonio'): 0,
    ('San Antonio', 'Fort Worth'): 68,
    ('San Antonio', 'El Paso'): 74,
    ('San Antonio', 'Arlington'): 43,
    ('San Antonio', 'Corpus Christi'): 22,
    ('San Antonio', 'Plano'): 78,
    ('San Antonio', 'Lubbock'): 81,
    ('San Antonio', 'Laredo'): 98,
    ('San Antonio', 'Irving'): 16,
    ('San Antonio', 'Garland'): 28,
    ('San Antonio', 'Frisco'): 23,
    ('San Antonio', 'Amarillo'): 91,
    ('San Antonio', 'Brownsville'): 96,
    ('San Antonio', 'Grand Prairie'): 98,
    ('San Antonio', 'McAllen'): 92,
    ('San Antonio', 'Pasadena'): 85,
    ('San Antonio', 'Mesquite'): 46,
    ('Fort Worth', 'Fort Worth'): 0,
    ('Fort Worth', 'El Paso'): 27,
    ('Fort Worth', 'Arlington'): 66,
    ('Fort Worth', 'Corpus Christi'): 4,
    ('Fort Worth', 'Plano'): 48,
    ('Fort Worth', 'Lubbock'): 99,
    ('Fort Worth', 'Laredo'): 61,
    ('Fort Worth', 'Irving'): 94,
    ('Fort Worth', 'Garland'): 38,
    ('Fort Worth', 'Frisco'): 50,
    ('Fort Worth', 'Amarillo'): 56,
    ('Fort Worth', 'Brownsville'): 43,
    ('Fort Worth', 'Grand Prairie'): 52,
    ('Fort Worth', 'McAllen'): 79,
    ('Fort Worth', 'Pasadena'): 33,
    ('Fort Worth', 'Mesquite'): 26,
    ('El Paso', 'El Paso'): 0,
    ('El Paso', 'Arlington'): 88,
    ('El Paso', 'Corpus Christi'): 89,
    ('El Paso', 'Plano'): 85,
    ('El Paso', 'Lubbock'): 83,
    ('El Paso', 'Laredo'): 39,
    ('El Paso', 'Irving'): 73,
    ('El Paso', 'Garland'): 87,
    ('El Paso', 'Frisco'): 21,
    ('El Paso', 'Amarillo'): 68,
    ('El Paso', 'Brownsville'): 17,
    ('El Paso', 'Grand Prairie'): 98,
    ('El Paso', 'McAllen'): 59,
    ('El Paso', 'Pasadena'): 98,
    ('El Paso', 'Mesquite'): 48,
    ('Arlington', 'Arlington'): 0,
    ('Arlington', 'Corpus Christi'): 69,
    ('Arlington', 'Plano'): 48,
    ('Arlington', 'Lubbock'): 13,
    ('Arlington', 'Laredo'): 11,
    ('Arlington', 'Irving'): 83,
    ('Arlington', 'Garland'): 26,
    ('Arlington', 'Frisco'): 94,
    ('Arlington', 'Amarillo'): 46,
    ('Arlington', 'Brownsville'): 13,
    ('Arlington', 'Grand Prairie'): 63,
    ('Arlington', 'McAllen'): 91,
    ('Arlington', 'Pasadena'): 26,
    ('Arlington', 'Mesquite'): 86,
    ('Mesquite', 'Mesquite'): 0,
    ('Corpus Christi', 'Corpus Christi'): 0,
    ('Corpus Christi', 'Plano'): 35,
    ('Corpus Christi', 'Lubbock'): 38,
    ('Corpus Christi', 'Laredo'): 7,
    ('Corpus Christi', 'Irving'): 63,
    ('Corpus Christi', 'Garland'): 7,
    ('Corpus Christi', 'Frisco'): 40,
    ('Corpus Christi', 'Amarillo'): 63,
    ('Corpus Christi', 'Brownsville'): 75,
    ('Corpus Christi', 'Grand Prairie'): 64,
    ('Corpus Christi', 'McAllen'): 84,
    ('Corpus Christi', 'Pasadena'): 78,
    ('Corpus Christi', 'Mesquite'): 10,
    ('Plano', 'Plano'): 0,
    ('Plano', 'Lubbock'): 91,
    ('Plano', 'Laredo'): 29,
    ('Plano', 'Irving'): 82,
    ('Plano', 'Garland'): 81,
    ('Plano', 'Frisco'): 41,
    ('Plano', 'Amarillo'): 94,
    ('Plano', 'Brownsville'): 16,
    ('Plano', 'Grand Prairie'): 7,
    ('Plano', 'McAllen'): 77,
    ('Plano', 'Pasadena'): 4,
    ('Plano', 'Mesquite'): 94,
    ('Lubbock', 'Lubbock'): 0,
    ('Lubbock', 'Laredo'): 21,
    ('Lubbock', 'Irving'): 75,
    ('Lubbock', 'Garland'): 29,
    ('Lubbock', 'Frisco'): 84,
    ('Lubbock', 'Amarillo'): 83,
    ('Lubbock', 'Brownsville'): 61,
    ('Lubbock', 'Grand Prairie'): 60,
    ('Lubbock', 'McAllen'): 55,
    ('Lubbock', 'Pasadena'): 81,
    ('Lubbock', 'Mesquite'): 62,
    ('Laredo', 'Laredo'): 0,
    ('Laredo', 'Irving'): 13,
    ('Laredo', 'Garland'): 41,
    ('Laredo', 'Frisco'): 83,
    ('Laredo', 'Amarillo'): 55,
    ('Laredo', 'Brownsville'): 14,
    ('Laredo', 'Grand Prairie'): 41,
    ('Laredo', 'McAllen'): 13,
    ('Laredo', 'Pasadena'): 80,
    ('Laredo', 'Mesquite'): 95,
    ('Irving', 'Irving'): 0,
    ('Irving', 'Garland'): 96,
    ('Irving', 'Frisco'): 41,
    ('Irving', 'Amarillo'): 46,
    ('Irving', 'Brownsville'): 76,
    ('Irving', 'Grand Prairie'): 18,
    ('Irving', 'McAllen'): 46,
    ('Irving', 'Pasadena'): 88,
    ('Irving', 'Mesquite'): 76,
    ('Garland', 'Garland'): 0,
    ('Garland', 'Frisco'): 66,
    ('Garland', 'Amarillo'): 44,
    ('Garland', 'Brownsville'): 100,
    ('Garland', 'Grand Prairie'): 94,
    ('Garland', 'McAllen'): 60,
    ('Garland', 'Pasadena'): 12,
    ('Garland', 'Mesquite'): 51,
    ('Frisco', 'Frisco'): 0,
    ('Frisco', 'Amarillo'): 6,
    ('Frisco', 'Brownsville'): 95,
    ('Frisco', 'Grand Prairie'): 60,
    ('Frisco', 'McAllen'): 82,
    ('Frisco', 'Pasadena'): 94,
    ('Frisco', 'Mesquite'): 10,
    ('Amarillo', 'Amarillo'): 0,
    ('Amarillo', 'Brownsville'): 54,
    ('Amarillo', 'Grand Prairie'): 43,
    ('Amarillo', 'McAllen'): 73,
    ('Amarillo', 'Pasadena'): 62,
    ('Amarillo', 'Mesquite'): 42,
    ('Brownsville', 'Brownsville'): 0,
    ('Brownsville', 'Grand Prairie'): 59,
    ('Brownsville', 'McAllen'): 34,
    ('Brownsville', 'Pasadena'): 27,
    ('Brownsville', 'Mesquite'): 47,
    ('Grand Prairie', 'Grand Prairie'): 0,
    ('Grand Prairie', 'McAllen'): 64,
    ('Grand Prairie', 'Pasadena'): 56,
    ('Grand Prairie', 'Mesquite'): 8,
    ('McAllen', 'McAllen'): 0,
    ('McAllen', 'Pasadena'): 34,
    ('McAllen', 'Mesquite'): 18,
    ('Pasadena', 'Pasadena'): 0,
    ('Pasadena', 'Mesquite'): 8
}

cities = {name: City(name) for name in texas_cities_names}

for (city1, city2), distance in real_distances.items():
    if city1 in cities and city2 in cities:
        cities[city1].add_city(cities[city2], distance)
        cities[city2].add_city(cities[city1], distance)



graph = nx.Graph()

for city in texas_cities_names:
    if city not in graph.nodes:
        graph.add_node(city)

for (city1, city2), distance in real_distances.items():
    graph.add_edge(city1, city2, weight=distance)

tsp_path = christofides(graph)

for city in texas_cities_names:
    if city not in graph.nodes:
        graph.add_node(city)

# Ensure all edges have weights
for city1 in texas_cities_names:
    for city2 in texas_cities_names:
        if city1 != city2 and not graph.has_edge(city1, city2):
            graph.add_edge(city1, city2, weight=1000)  # Default weight for missing distances

# Verify graph completeness
for city1 in texas_cities_names:
    for city2 in texas_cities_names:
        assert graph.has_edge(city1, city2), f"Edge missing: {city1}-{city2}"

tsp_cost = sum(
    graph[u][v]["weight"] for u, v in zip(tsp_path, tsp_path[1:] + [tsp_path[0]])
)

print("TSP Path (Approximation):")
print(" -> ".join(tsp_path))
print(f"Total Cost: {tsp_cost} km")


def nearest_neighbor(graph, start_node):
    visited = {start_node}
    path = [start_node]
    current_node = start_node

    while len(visited) < len(graph.nodes):
        nearest_city = None
        min_distance = float('inf')
        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                distance = graph[current_node][neighbor]["weight"]
                if distance < min_distance:
                    min_distance = distance
                    nearest_city = neighbor
        visited.add(nearest_city)
        path.append(nearest_city)
        current_node = nearest_city

    path.append(start_node)
    return path

graph = nx.Graph()
for (city1, city2), distance in real_distances.items():
    graph.add_edge(city1, city2, weight=distance)

start_city = "Houston"
tsp_path = nearest_neighbor(graph, start_city)

tsp_cost = sum(graph[u][v]["weight"] for u, v in zip(tsp_path, tsp_path[1:]))

print("TSP Path (Nearest Neighbor):")
print(" -> ".join(tsp_path))
print(f"Total Cost: {tsp_cost} km")





