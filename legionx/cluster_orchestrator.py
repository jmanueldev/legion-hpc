from legionx.node_orchestrator import NodeOrchestrator

class ClusterOrchestrator:
    """
    Manages a group of nodes (Legion Commanders)
    """
    def __init__(self, name: str, nodes: list[NodeOrchestrator]):
        self.name = name
        self.nodes = nodes
        self.capacity = sum(n.capacity for n in nodes)

    def assign_tasks(self, num_tasks: int):
        """
        Distribute tasks among nodes using simple round-robin.
        """
        for i in range(num_tasks):
            node = self.nodes[i % len(self.nodes)]
            node.execute_task(f"Task-{i+1}")
        print(f"[Cluster {self.name}] Assigned {num_tasks} tasks to nodes")
