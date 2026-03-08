import numpy as np
import gym
from gym import spaces
from legionx.cluster_orchestrator import ClusterOrchestrator

class HPCEnv(gym.Env):
    """
    Gym environment representing clusters as RL environment
    Actions: Allocate tasks to clusters
    Observations: Cluster load levels
    """
    def __init__(self, clusters: list[ClusterOrchestrator], max_tasks=10):
        super().__init__()
        self.clusters = clusters
        self.max_tasks = max_tasks
        self.action_space = spaces.Discrete(len(clusters))  # Choose cluster
        self.observation_space = spaces.Box(low=0, high=max_tasks, shape=(len(clusters),), dtype=np.int32)

    def reset(self):
        self.state = np.zeros(len(self.clusters), dtype=np.int32)
        return self.state

    def step(self, action):
        # Assign 1 task to selected cluster
        self.state[action] += 1
        reward = -np.std(self.state)  # Reward is negative load imbalance
        done = np.sum(self.state) >= self.max_tasks
        return self.state, reward, done, {}

# Example usage
if __name__ == "__main__":
    from legionx.node_orchestrator import NodeOrchestrator
    from legionx.compute_node import ComputeNode
    from stable_baselines3 import DQN

    # Create dummy clusters
    clusters = []
    for i in range(2):
        nodes = [NodeOrchestrator(f"Node{i}{j}", ComputeNode(f"Node{i}{j}")) for j in range(3)]
        clusters.append(ClusterOrchestrator(f"Cluster{i}", nodes))

    env = HPCEnv(clusters)
    model = DQN("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=1000)

    obs = env.reset()
    for _ in range(10):
        action, _states = model.predict(obs)
        obs, reward, done, info = env.step(action)
        print(f"Action: {action}, State: {obs}, Reward: {reward}")
        if done:
            obs = env.reset()
