import numpy as np
from legionx.cluster_orchestrator import ClusterOrchestrator

class StrategicOrchestrator:
    """
    Strategic layer: Makes AI-driven global decisions.
    """
    def __init__(self, clusters: list[ClusterOrchestrator]):
        self.clusters = clusters
        self.history = []

    def plan_campaign(self, workload: dict):
        """
        Distribute workload to clusters using predictive heuristics or RL.
        workload example: {'task_name': 'simulation', 'size': 10}
        """
        # Simple proportional allocation (placeholder for RL)
        total_capacity = sum(c.capacity for c in self.clusters)
        for cluster in self.clusters:
            fraction = cluster.capacity / total_capacity
            cluster.assign_tasks(int(workload['size'] * fraction))
        self.history.append(workload)
        print(f"[Strategic] Campaign planned: {workload}")
