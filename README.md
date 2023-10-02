# Inter Vehicle Coordination

A project focused on simulating coordination and communication strategies among vehicles in a dynamic environment, employing reinforcement learning techniques to optimize vehicle behavior and interactions.

***
### Layers :
#### • Input Layer: 
The input layer receives the normalized state information of the focal vehicle and nearby vehicles within its communication radius, which serves as the initial input for the neural network.

#### • LSTM (Long Short-Term Memory) Layer: 
The LSTM layer captures temporal dependencies in the data, allowing the model to consider the sequence of states and make informed decisions based on past and current information.

#### • Dense Layer (Output Layer): 
The dense layer, the output layer, produces Q-values for different actions the focal vehicle can take, enabling it to estimate the expected rewards associated with each action.

#### These layers work in concert to enable the deep Q-network (DQN) to learn and optimize the decision-making process of the focal vehicle in the context of inter-vehicle coordination and communication.

***
### Gen-1 Iteration:
• Same speed and Communication radius for every vehicle <br/>
• Relate longitude and latitude using a 2 Dimensional matrix

### Dependencies:
The following dependencies are required to run the project:

• Python (version 3.7 or above) <br/>
• NumPy (version 1.21.0 or above) <br/>
• keras <br/>
• TensorFlow <br/>
