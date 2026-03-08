import random

def collect_telemetry(node_name: str):
    """
    Simulate real-time telemetry collection
    """
    return {
        'node': node_name,
        'cpu_load': random.randint(0, 100),
        'memory_load': random.randint(0, 100),
        'network_latency': random.uniform(0, 10)
    }
