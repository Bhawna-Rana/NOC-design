# NOC-design
## Reinforcement Learning Design Document
### State:
Buffer Occupancy: Percentage occupancy of each buffer.
Arbitration Rates: Current arbitration rates at the input of the arbiter for CPU and IO.
Power Threshold Status: Whether the system power exceeds the threshold or not.
Latency: Current measured latency.
Bandwidth: Current measured bandwidth.
Throttling Status: Whether throttling is currently active or not.
### Actions:
Adjust Buffer Sizes: Increase or decrease buffer sizes.
Adjust Arbiter Weights: Change weights of the arbiter for CPU and IO.
Throttle or De-throttle: Adjust operating frequency.
### Rewards:
Low Latency: Positive reward for achieving latency <= min_latency.
High Bandwidth: Positive reward for achieving bandwidth >= 95% of max_bandwidth.
Buffer Occupancy: Positive reward for maintaining buffer occupancy around 90%.
Minimized Throttling: Positive reward for keeping throttling to 5% or less.
Low Power Consumption: Positive reward for staying below power threshold.
Penalties: Negative rewards for violating any of the above conditions.
### RL Algorithm:
Given the complexity and continuous action space of this problem, a model-free RL algorithm like Deep Q-Network (DQN) or Actor-Critic would be suitable. DQN can efficiently handle the high-dimensional state space and continuous action space while learning an optimal policy. Actor-Critic methods can also effectively balance exploration and exploitation in this problem scenario.

### Training Procedure:
State Representation: Encode the current state variables into a suitable format for the RL algorithm.
Action Selection: Based on the current state, select actions using the RL policy.
Environment Interaction: Apply selected actions in the simulator and observe the resulting rewards and next state.
Update Q-values or Policy: Update the Q-values or policy based on observed rewards and transitions.
Repeat: Iterate through steps 2-4 until convergence or a predefined number of iterations.
Testing and Validation: Evaluate the learned policy on test workloads to ensure generalization and effectiveness. Adjust parameters as necessary.
### Conclusion:
By implementing an RL framework with suitable states, actions, and rewards, along with an appropriate RL algorithm like DQN or Actor-Critic, it's possible to optimize the NOC design to meet the specified requirements efficiently. The RL agent will learn to dynamically adjust system parameters to achieve the desired performance metrics while considering system constraints and workload variations.


