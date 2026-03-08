import random
import time

class ComputeNode:
    """
    Simulates a compute node (Soldier)
    """
    def __init__(self, name: str, capacity: int = 1):
        self.name = name
        self.capacity = capacity

    def run(self, task_name: str):
        print(f"[Node {self.name}] Running {task_name}")
        # Simulate execution time
        time.sleep(random.uniform(0.1, 0.5))
        print(f"[Node {self.name}] Completed {task_name}")
