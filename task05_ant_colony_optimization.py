"""
Task 5: Ant Colony Optimization (ACO)
Aim: Demonstrate pheromone-guided path selection on a small graph.
This simple version chooses the best of two possible routes.
"""

import random


def ant_colony_optimization(iterations=20, ants=10, seed=1):
    random.seed(seed)

    # Two routes from Start to Goal, represented by their distances.
    routes = {"Route A": 4, "Route B": 7}
    pheromone = {route: 1.0 for route in routes}
    evaporation = 0.3
    alpha = 1.0
    beta = 2.0

    for _ in range(iterations):
        route_counts = {route: 0 for route in routes}

        for _ in range(ants):
            weights = {
                route: (pheromone[route] ** alpha) * ((1 / distance) ** beta)
                for route, distance in routes.items()
            }
            chosen = random.choices(
                list(routes), weights=list(weights.values()), k=1
            )[0]
            route_counts[chosen] += 1

        for route in routes:
            pheromone[route] *= (1 - evaporation)
            pheromone[route] += route_counts[route] / routes[route]

    best_route = min(routes, key=lambda route: routes[route])
    return best_route, routes[best_route], pheromone


def main():
    route, distance, pheromone = ant_colony_optimization()
    print("Best route:", route)
    print("Route distance:", distance)
    print("Final pheromone levels:", {
        key: round(value, 3) for key, value in pheromone.items()
    })


if __name__ == "__main__":
    main()
