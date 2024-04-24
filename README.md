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
Adjust Arbiter Weights: Change the weights of the arbiter for CPU and IO.
Throttle or De-throttle: Adjust operating frequency.
### Rewards:
Low Latency: Positive reward for achieving latency <= min_latency.
High Bandwidth: Positive reward for achieving bandwidth >= 95% of max_bandwidth.
Buffer Occupancy: Positive reward for maintaining buffer occupancy around 90%.
Minimized Throttling: Positive reward for keeping throttling to 5% or less.
Low Power Consumption: Positive reward for staying below the power threshold.
Penalties: Negative rewards for violating any of the above conditions.
### RL Algorithm:
Given the complexity and continuous action space of this problem, a model-free RL algorithm like Deep Q-Network (DQN) or Actor-Critic would be suitable. DQN can efficiently handle the high-dimensional state space and continuous action space while learning an optimal policy. Actor-critic methods can also effectively balance exploration and exploitation in this problem scenario.

### Training Procedure:
State Representation: Encode the current state variables into a suitable format for the RL algorithm.
Action Selection: Based on the current state, select actions using the RL policy.
Environment Interaction: Apply selected actions in the simulator and observe the resulting rewards and next state.
Update Q-values or Policy: Update the Q-values or policy based on observed rewards and transitions.
Repeat: Iterate through steps 2-4 until convergence or a predefined number of iterations.
Testing and Validation: Evaluate the learned policy on test workloads to ensure generalization and effectiveness. Adjust parameters as necessary.
### Conclusion:
By implementing an RL framework with suitable states, actions, and rewards, along with an appropriate RL algorithm like DQN or Actor-Critic, optimizing the NOC design to meet the specified requirements efficiently is possible. The RL agent will learn to dynamically adjust system parameters to achieve the desired performance metrics while considering system constraints and workload variations.

## Latency and bandwidth calculation

### Problem Statement
In the proposed solution, I am providing a method to efficiently measure latency and bandwidth using pseudocode from simulated interface monitor output. This is essential for understanding the performance of the NOC design under different workloads and system configurations. The goal is to optimize the NOC design to meet specified performance criteria while minimizing resource usage and power consumption. Also, I'd like to suggest the implementation of a Reinforcement Learning (RL) framework to adjust system parameters based on observed performance and feedback dynamically. This approach aims to automate the optimization process and enable the NOC to adapt to varying workload conditions in real-time. Ultimately, this solution serves SoC designers and engineers tasked with developing efficient and high-performance computing systems. One more industrial implication of this solution is embedded systems design, particularly for applications requiring real-time processing and stringent performance requirements. For example, in automotive systems where onboard computers manage numerous tasks such as engine control, driver assistance, and infotainment, optimizing the NOC design can enhance overall system responsiveness and reliability. By dynamically adjusting system parameters based on workload characteristics, the proposed solution can ensure consistent and efficient data communication between different components within the SoC, leading to improved vehicle performance, safety, and user experience.

### Approach for Algorithm design
The approach used to generate the algorithm/design combines both traditional methods and modern techniques:

1. Understanding the Problem: A thorough comprehension of the problem statement and its requirements is crucial. This involves breaking down the problem into its components, understanding the constraints, and identifying key performance metrics.

2. Traditional Methods for Pseudocode: For the pseudocode to measure latency and bandwidth, traditional algorithmic thinking was employed. This involved analyzing the input data format, defining variables and calculations needed, and structuring the code clearly and efficiently.

3. Modern Techniques for Reinforcement Learning: Modern techniques from machine learning and AI were utilized for the RL framework design. This involved defining states, actions, and rewards based on the problem requirements, selecting a suitable RL algorithm (DQN or Actor-Critic), and designing a training procedure to optimize the NOC design.
4. Integration and Iteration: The traditional and modern approaches were integrated iteratively. The pseudocode for measuring latency and bandwidth informed the design of the RL framework by identifying relevant states and rewards. Similarly, insights from RL theory were used to refine the pseudocode, such as considering dynamic adjustments based on observed performance.

5. Testing and Validation: Testing and validation were essential throughout the process. This involved simulating different scenarios, verifying the correctness and efficiency of the pseudocode, and evaluating the effectiveness of the RL framework in optimizing the NOC design against predefined performance criteria.

By combining traditional algorithmic thinking with modern techniques like Reinforcement Learning, the approach aimed to address the complexity and dynamic nature of the problem while ensuring practicality and efficiency in the solution design.

<img src = "https://github.com/Bhawna-Rana/NOC-design/blob/main/Mind%20map%20-%20Page%201.jpeg">

### Proof of Correctness
1. Adherence to Requirements:
The pseudocode correctly parses the simulated interface monitor output, identifying transaction types, timestamps, and data transfers.
It accurately calculates latency for read and write transactions, considering each transaction's start and end timestamps. Bandwidth is computed by tracking the total bytes transferred over all transactions and dividing by the total number of transactions.
2. Efficiency:
The pseudocode efficiently iterates through the interface monitor output, processing each line only once.
Latency calculations are performed without redundant operations, and bandwidth is computed using minimal memory and computational resources.
3. Validation Against Test Cases:
The correctness of the pseudocode can be validated against simulated test cases with known input-output pairs. Its accuracy can be verified by comparing the pseudocode's output against the expected latency and bandwidth values for these test cases.
4. Robustness:
The pseudocode handles various transaction types (reads and writes) and is adaptable to different data transfer scenarios. It accounts for potential edge cases, such as incomplete transactions or missing data, by defining clear latency and bandwidth calculation conditions.

### Complexity Analysis
1. Input Size:
The input size depends on the number of lines in the interface monitor output, which is proportional to the number of transactions simulated.
2. Latency Calculation:
The latency calculation involves iterating through each line of the interface monitor output once.
Reading transactions require searching for the corresponding data line to determine the end timestamp.
As each line is processed once, the time complexity for latency calculation is O(n), where n is the number of transactions.
3. Bandwidth Calculation:
The bandwidth calculation also involves iterating through each line of the interface monitor output once.
It calculates the total bytes transferred and divides by the total transactions.
Similar to latency calculation, the time complexity for bandwidth calculation is O(n).
Overall Complexity:
Considering both latency and bandwidth calculations, the overall time complexity of the pseudocode is O(n), where n is the number of transactions in the interface monitor output.
The space complexity is O(1) since the pseudocode only requires constant memory for storing variables and calculations, regardless of the input size.

### Alternatives Considered
One alternative approach could involve statistical analysis techniques such as regression or moving averages to estimate average latency and bandwidth over time. However, statistical methods may introduce additional complexity and may not accurately capture the system's dynamic behavior in real-time.

Another approach could be to train machine learning models, such as recurrent neural networks (RNNs) or long short-term memory (LSTM) networks, to predict latency and bandwidth based on historical data.
While machine learning models have the potential to capture complex patterns in the data, they often require large amounts of labeled training data. They may be computationally expensive to train and deploy.

Optimization algorithms such as genetic algorithms or simulated annealing could be employed to search for optimal parameter configurations iteratively.
While these algorithms offer the potential for finding near-optimal solutions, they often require significant computational resources and may not guarantee global optimality.
