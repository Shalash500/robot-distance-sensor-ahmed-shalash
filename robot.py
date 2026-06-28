"""
Robot Distance Sensor Program
This program reads a list of distance measurements (in meters) from a robot's front sensor.
It decides the robot's action based on the distance:
- STOP if the distance is less than 0.5m.
- SLOW if the distance is between 0.5m and 1.0m.
- MOVE if the distance is greater than 1.0m.
"""

# Creating a Robot Class
class Robot:
    def __init__(self, name, battery):
        # Initializes the Robot with a specific name and battery level.
        self.name = name
        self.battery = battery

    def process_distances(self, distances):

        """
        Processes a list of distance readings and returns a list of corresponding actions.
        Includes error handling to skip invalid or negative distance values.
        """
        actions = []

        for distance in distances:
            try:
                # Ensure the distance is a valid number
                dist = float(distance)         
                if dist < 0:
                    print(f"Warning: Negative distance ({distance}) ignored.")
                    continue
                    
                # Determine action based on distance
                if dist < 0.5:
                    actions.append("STOP")
                elif 0.5 <= dist <= 1.0:
                    actions.append("SLOW")
                else:
                    actions.append("MOVE")
                    
            except (ValueError, TypeError):
                print(f"Error: Invalid distance value '{distance}' encountered.")
                
        return actions

my_robot = Robot(name="ROS2_Bot", battery=100)

print(f"Testing {my_robot.name} (Battery: {my_robot.battery}%)\n")

# Test Case 1: The provided example
test_1 = [0.3, 1.5, 0.8, 2.0, 0.4]
print("Test 1 :", test_1)
print("Output:", my_robot.process_distances(test_1))
print("-" * 30)

# Test Case 2: All obstacles are very close
test_2 = [0.1, 0.2, 0.4]
print("Test 2 (All Too Close):", test_2)
print("Output:", my_robot.process_distances(test_2))
print("-" * 30)

# Test Case 3: All paths are completely clear
test_3 = [2.5, 5.0, 10.0]
print("Test 3 (All Clear):", test_3)
print("Output:", my_robot.process_distances(test_3))
print("-" * 30)

# Test Case 4: Edge cases (exactly 0.5 and 1.0)
test_4 = [0.5, 1.0]
print("Test 4 (Edge Cases):", test_4)
print("Output:", my_robot.process_distances(test_4))
print("-" * 30)

# Test Case 5: Error handling with bad data (strings and negative numbers)
test_5 = [0.6, "bad_data", -1.5, None, 1.2]
print("Test 5 (Bad Data / Error Handling):", test_5)
print("Output:", my_robot.process_distances(test_5))