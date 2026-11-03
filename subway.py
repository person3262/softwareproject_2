class Subway:
    def __init__(self, stations):
        self.graph = {}
        self.edge_line = {}

        stations.sort()
        for i in range(len(stations) - 1):
            if stations[i][0] == stations[i + 1][0]:
                a = self.short_name(stations[i][2])
                b = self.short_name(stations[i + 1][2])
                self.add_edge(a, b, stations[i][0])

    def short_name(self, name):
        return name.split('(')[0]

    def add_edge(self, a, b, line):
        if a not in self.graph:
            self.graph[a] = []
        if b not in self.graph:
            self.graph[b] = []
            
        self.graph[a].append(b)
        self.graph[b].append(a)
        self.edge_line[(a, b)] = line
        self.edge_line[(b, a)] = line

    def has_station(self, name):
        return name in self.graph

    def dfs_recursive(self, start, end, visited, all_paths):
        visited.append(start)

        if start == end:
            all_paths.append(visited[:])
        else:
            for node in self.graph[start]:
                if node not in visited:
                    self.dfs_recursive(node, end, visited, all_paths)

        visited.pop()

    def find_all_routes(self, start, end):
        all_paths = []
        self.dfs_recursive(start, end, [], all_paths)
        
        routes = [self.make_route(path) for path in all_paths]
        routes.sort()
        return routes

    def make_route(self, path):
        lines = [self.edge_line[(path[i], path[i + 1])] for i in range(len(path) - 1)]

        transfer_count = 0
        for i in range(len(lines) - 1):
            if lines[i] != lines[i + 1]:
                transfer_count += 1

        stop_count = len(lines)
        minutes = stop_count * 2 + transfer_count * 8
        return [minutes, transfer_count, stop_count, path, lines]

    def route_to_text(self, route):
        minutes, transfer_count, stop_count, path, lines = route

        text = f"{path[0]}({lines[0]})"
        for i in range(len(lines) - 1):
            if lines[i] != lines[i + 1]:
                text += f"-{path[i + 1]}(환승 {lines[i + 1]})"
        
        text += f"-{path[-1]}: {stop_count}역, {transfer_count}환승, {minutes}분"
        return text