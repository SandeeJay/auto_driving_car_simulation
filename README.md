# Auto Driving Car Simulation

## Overview

A simulation program for autonomous driving cars on a grid. Users can add cars, issue commands, and simulate movement with collision detection and boundary constraints.

## Features

- Add cars to the simulation with unique names.
- Set commands for each car to control their movement.
- Run the simulation and observe the final positions and directions of the cars.
- Detect and report collisions between cars and boundaries.

## Requirements

- Python 3.6+
- `pytest` for running tests

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/SandeeJay/auto_driving_car_simulation.git
    cd auto-driving-car-simulation
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the simulation, execute the `main.py` file:
```sh
python main.py
```
Follow the on-screen instructions to set up the field, add cars, and run the simulation.

## Running Tests

To run the tests, use pytest:
```sh
python -m pytest    
```
## Project Structure
- main.py: The main entry point for running the simulation.
- src/: Contains the source code for the simulation.
  - car.py: Defines the Car class.
  - field.py: Defines the Field class.
  - simulation.py: Defines the Simulation class.
- tests/: Contains the test cases for the project.
  - test_car.py: Tests for the Car class.
  - test_field.py: Tests for the Field class.
  - test_simulation.py: Tests for the Simulation class.

## Assumptions
- Application will exit if invalid input provided
- Car name is mandatory and unique
- Stop moving the car if the new coordinate detected is outside the specified field size or collides with another car