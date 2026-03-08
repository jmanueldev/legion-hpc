from legionx.compute_node import ComputeNode
from legionx.telemetry import collect_telemetry

class NodeOrchestrator:
    def __init__(self, name: str, node: ComputeNode):
        self.name = name
        self.node = node
        self.capacity = node.capacity

    def execute_task(self, task_name: str):
        metrics = collect_telemetry(self.node.name)
        if metrics['cpu_load'] < 90:  # self-healing check
            self.node.run(task_name)
        else:
            print(f"[Node {self.name}] CPU too high, rescheduling {task_name}")
