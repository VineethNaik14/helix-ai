class DependencyGraph:
    def build(self, python_metadata: dict):
        graph = {}

        for file_name, metadata in python_metadata.items():
            graph[file_name] = metadata.get("imports", [])

        return graph


dependency_graph = DependencyGraph()
