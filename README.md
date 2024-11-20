# Christofides Algorithm for Solving the Traveling Salesman Problem

This repository contains an implementation of the **Christofides algorithm** to solve the **Traveling Salesman Problem (TSP)**. The algorithm is a polynomial-time approximation algorithm that guarantees a solution within 3/2 of the optimal solution for the metric TSP.

## Key Features
- **Christofides Algorithm** for TSP approximation.
- **Graph completion** to ensure that the graph is fully connected, which is required for the algorithm to work.
- **Automatic missing edge addition** to make sure the graph is complete, ensuring all nodes are connected.

## Files and Functions
1. **christofides.py**: Contains the implementation of the Christofides algorithm.
2. **graph.py**: Defines a graph structure for cities and the distances between them.
3. **make_graph_complete.py**: A utility to automatically add missing edges between nodes to complete the graph.

## Requirements
- Python 3.x
- NetworkX library for graph-related operations.

You can install the necessary dependencies using:

```bash
pip install networkx

## How to Use

### 1. Define Cities and Edges

In the `graph.py` file, define the cities and their pairwise distances like this:

```python
self.cities["A"].add_city(self.cities["B"], 10)
self.cities["A"].add_city(self.cities["C"], 15)
self.cities["B"].add_city(self.cities["C"], 35)
self.cities["B"].add_city(self.cities["D"], 25)
self.cities["C"].add_city(self.cities["D"], 30)
```

# Christofides Algorithm for Solving the Traveling Salesman Problem (TSP)

This guide outlines how to apply the Christofides algorithm to solve the Traveling Salesman Problem (TSP) for a set of cities with pairwise distances.

## 1. Define Pairwise Distances
First, define the distances between each city. You can create a graph where each city is a node, and the edges represent the distance between pairs of cities.

## 2. Complete the Graph
The Christofides algorithm requires a complete graph (i.e., every pair of cities must be connected by an edge). If some cities are not directly connected, you can use the `make_graph_complete.py` script to automatically add missing edges with a default weight.

### `make_graph_complete.py`

```python
def make_graph_complete(graph, default_weight=50):
    from itertools import combinations
    
    nodes = list(graph.nodes)
    for u, v in combinations(nodes, 2):
        if not graph.has_edge(u, v):
            graph.add_edge(u, v, weight=default_weight)
            print(f"Added missing edge ({u}, {v}) with weight {default_weight}")
```

You can call this function to ensure the graph is complete:

```python
make_graph_complete(self.graph, default_weight=50)
```

This will add the missing edges to the graph with a default weight (e.g., 50).

## 2. Run Christofides Algorithm
Once the graph is complete, you can now run the Christofides algorithm to solve the TSP. This is done by passing the complete graph to the `christofides()` function:

```python
tsp_path = christofides(self.graph)
```

This will return the TSP path, which is an approximation of the optimal path for visiting all cities.

## 3. Example Output
After running the algorithm, you should see an output like this:

```rust
TSP Path (Approximation):
Houston -> Lubbock -> Austin -> San Antonio -> Irving -> Laredo -> McAllen -> Mesquite -> Grand Prairie -> Plano -> Pasadena -> Garland -> Corpus Christi -> Frisco -> Amarillo -> Dallas -> Arlington -> El Paso -> Brownsville -> Fort Worth -> Houston
Total Cost: 398 km

TSP Path (Nearest Neighbor):
Houston -> Fort Worth -> Corpus Christi -> Laredo -> Austin -> Lubbock -> Arlington -> Brownsville -> Plano -> Pasadena -> Mesquite -> Grand Prairie -> Irving -> San Antonio -> Frisco -> Amarillo -> Garland -> Dallas -> El Paso -> McAllen -> Houston
Total Cost: 482 km
```

Here’s your content converted to GitHub-flavored Markdown:

markdown
## 4. Summary
1. **Step 1**: Define your cities and pairwise distances.
2. **Step 2**: Use the `make_graph_complete()` function to ensure the graph is complete.
3. **Step 3**: Call the `christofides()` function to find the TSP path.
4. **Step 4**: Check the output for the TSP path and its total cost.

Now, you can use this structure to apply the Christofides algorithm to any graph and solve the TSP approximation problem.
