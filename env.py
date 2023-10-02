import numpy as np
import random

class CustomEnvironment:
    def __init__(self, x=None, y=None, xd=None, yd=None, direction=None, velocity = 1, communication_radius=3, grid_size=(100, 100)):
        self.communication_radius = communication_radius
        self.grid_size = grid_size

        # Initialization
        self.state = None
        self.destination = None
        self.communication_radius = communication_radius
        self.actions = [0, 1, 2, 3]  # Actions (0: North, 1: South, 2: East, 3: West)
        self.direction = direction
        self.velocity = velocity
        self.stationary_vehicles = []
        self.max_velocity = 1
        self.num_vehicles = int(grid_size[0] * grid_size[1] * 0.05)
        self.vehicle_count = np.zeros(self.grid_size, dtype=int)

        if x is not None and y is not None:
            self.initialize_state(x, y)
        if xd is not None and yd is not None:
            self.set_destination(xd, yd)

    def reset(self):
        self.initialize_state()
        self.set_destination()
        self.set_stationary_vehicles()
        self.set_direction()
        return self


    def initialize_state(self, x=None, y=None):
        if x == None or y == None:
          self.state = (random.randint(0, self.grid_size[0] - 1), random.randint(0, self.grid_size[1] - 1))
        else:
          self.state = (x, y)


    def set_num_vehicles(self, num_vehicles):
        self.num_vehicles = num_vehicles


    def set_destination(self, xd=None, yd=None):
        if xd == None or yd == None:
          while True:
                  xd, yd = random.randint(0, self.grid_size[0] - 1), random.randint(0, self.grid_size[1] - 1)
                  if self.state != (xd, yd):
                      self.destination = (xd, yd)
                      break
        else:
          self.destination = (xd, yd)

    def set_direction(self, direction=None):
      if direction == None:
        self.direction = random.randint(0, 3)
      else:
        self.direction = direction


    def set_stationary_vehicles(self):
            vehicle_positions = []
            vehicle_destinations = []

            for _ in range(self.num_vehicles):
              while True:
                  x, y = random.randint(0, self.grid_size[0] - 1), random.randint(0, self.grid_size[1] - 1)
                  if (x, y) not in vehicle_positions and (x, y) != self.state and (x, y) != self.destination:
                      vehicle_positions.append((x, y))
                      self.vehicle_count[(x, y)] += 1
                      break

            for i in range(self.num_vehicles):
                    while True:
                        xd, yd = random.randint(0, self.grid_size[0] - 1), random.randint(0, self.grid_size[1] - 1)
                        if vehicle_positions[i] != (xd, yd):
                            vehicle_destinations.append((xd, yd))
                            break

            for i in range(self.num_vehicles):
                    direction = random.randint(0, 3)
                    environment = CustomEnvironment(vehicle_positions[i][0], vehicle_positions[i][1], vehicle_destinations[i][0], vehicle_destinations[i][1], direction)
                    self.stationary_vehicles.append(environment)


    def step(self, action):

        x, y = self.state[0], self.state[1]

        nx, ny = x, y

        if action == 0:  # North
            ny = (y - 1)
        elif action == 1:  # South
            ny = (y + 1)
        elif action == 2:  # East
            nx = (x + 1)
        elif action == 3:  # West
            mx = (x - 1)


        reward = 0
        done = False

        if nx < 0 or ny < 0 or nx == self.grid_size[0] or ny == self.grid_size[1]:
          reward = -.2
          done = True
        elif (nx, ny) == self.destination:
          reward = 1
          self.state = (nx, ny)
          self.direction = action
          done = True
        elif self.vehicle_count[(nx, ny)] > 0:
          reward = -self.vehicle_count[(nx, ny)]
          self.state = (nx, ny)
          self.direction = action
        else:
          reward = 0.05
          self.state = (nx, ny)
          self.direction = action

        return self, reward, done

    def render(self):
        # a method to render
        pass
