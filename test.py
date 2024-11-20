import unittest
from main import *


class TestTSP(unittest.TestCase):

    def setUp(self):
        self.cities = {
            "A": City("A"),
            "B": City("B"),
            "C": City("C"),
            "D": City("D")
        }
        self.cities["A"].add_city(self.cities["B"], 10)
        self.cities["A"].add_city(self.cities["C"], 15)
        self.cities["A"].add_city(self.cities["D"], 50)
        self.cities["B"].add_city(self.cities["C"], 35)
        self.cities["B"].add_city(self.cities["D"], 25)
        self.cities["C"].add_city(self.cities["D"], 30)

        self.graph = nx.Graph()
        for city1 in self.cities.values():
            for city2, distance in city1.cities.items():
                self.graph.add_edge(city1.name, city2.name, weight=distance)

    def test_city_creation(self):
        city = City("X")
        city.add_city(self.cities["A"], 50)
        self.assertEqual(city.get_distance(self.cities["A"]), 50)
        self.assertIn(self.cities["A"], city.get_direct_cities())

    def test_graph_structure(self):
        """Test that the graph is correctly structured."""
        self.assertEqual(len(self.graph.nodes), 4)
        self.assertEqual(self.graph["A"]["B"]["weight"], 10)
        self.assertEqual(self.graph["C"]["D"]["weight"], 30)

    def test_christofides_algorithm(self):
        """Test Christofides approximation algorithm."""
        tsp_path = christofides(self.graph)
        self.assertIn("A", tsp_path)  # Check if the path includes starting node
        self.assertIn("B", tsp_path)  # Check if the path includes all nodes
        self.assertIn("C", tsp_path)
        self.assertIn("D", tsp_path)

    def test_nearest_neighbor_algorithm(self):
        """Test Nearest Neighbor heuristic."""
        tsp_path = nearest_neighbor(self.graph, "A")
        self.assertEqual(tsp_path[0], "A")  # Path should start at "A"
        self.assertEqual(tsp_path[-1], "A")  # Path should return to "A"
        self.assertEqual(len(tsp_path), len(self.graph.nodes) + 1)  # Check path length

    def test_tsp_cost_calculation(self):
        """Test TSP cost calculation."""
        tsp_path = nearest_neighbor(self.graph, "A")
        tsp_cost = sum(
            self.graph[u][v]["weight"] for u, v in zip(tsp_path, tsp_path[1:])
        )
        self.assertGreater(tsp_cost, 0)
        self.assertIsInstance(tsp_cost, int)

if __name__ == "__main__":
    unittest.main()
