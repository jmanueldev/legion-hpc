from legionx.compute_node import ComputeNode

class NodeOrchestrator:
    """
    Node-level controller (Centurions)
    """
    def __init__(self, name: str, node: ComputeNode):
        self.name = name
        self.node = node
        self.capacity = node.capacity

    def execute_task(self, task_name: str):
        """
        Execute task and collect telemetry
        """
        self.node.run(task_name)
