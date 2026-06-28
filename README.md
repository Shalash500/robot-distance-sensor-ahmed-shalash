# Robot Distance Sensor Program

## 1. What does this program do?
This program simulates a robot's decision-making process based on input from a front-facing distance sensor. It takes a list of distance measurements in meters and outputs a list of actions for the robot to take: `STOP` for distances under 0.5m, `SLOW` for distances between 0.5m and 1.0m, and `MOVE` for distances over 1.0m.

## 2. How does the Robot class work?
The `Robot` class serves as a blueprint for the robot object. When instantiated, it assigns a `name` and a `battery` percentage to the robot. It encapsulates the core logic needed to process sensor data through its built-in methods.

## 3. What does each method do?
- `__init__(self, name, battery)`: This is the constructor method. It initializes the robot object and stores the provided name and battery level as instance attributes.
- `process_distances(self, distances)`: This method loops through a provided list of distance readings. It uses `try-except` blocks to filter out bad data (like strings or null values) and ignores negative numbers. For valid numeric inputs, it applies the logical conditions to determine if the robot should STOP, SLOW, or MOVE, and appends that action to an output list which is then returned.

## 4. How do I run the code?
To run the code, ensure you have Python installed on your system. Open your terminal, navigate to the directory containing the file, and execute the following command:
`python3 robot.py`
The output of the 5 test cases will print directly to the console.

## 5. What did you learn from using AI?
Using AI helped structure the initial logic for reading lists and filtering data efficiently. It demonstrated how to properly implement `try-except` error handling blocks to catch `ValueError` and `TypeError` exceptions gracefully without crashing the entire script when bad sensor data is encountered.