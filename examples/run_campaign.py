from legionx.compute_node import ComputeNode
from legionx.node_orchestrator import NodeOrchestrator
from legionx.cluster_orchestrator import ClusterOrchestrator
from legionx.strategic_orchestrator import StrategicOrchestrator

# Create compute nodes
nodes_a = [NodeOrchestrator(f"NodeA{i}", ComputeNode(f"NodeA{i}")) for i in range(3)]
nodes_b = [NodeOrchestrator(f"NodeB{i}", ComputeNode(f"NodeB{i}")) for i in range(3)]

# Create clusters
cluster1 = ClusterOrchestrator("Alpha", nodes_a)
cluster2 = ClusterOrchestrator("Beta", nodes_b)

# Create strategic orchestrator
general = StrategicOrchestrator([cluster1, cluster2])

# Launch a campaign
general.plan_campaign({'task_name': 'Simulation', 'size': 10})
