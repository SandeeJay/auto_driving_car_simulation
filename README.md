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

2. Set Up a Virtual Environment (Optional but Recommended):

    Ensure you have Python installed on your system. It is recommended to use a virtual environment to keep dependencies organized and separate from other projects.
    ```sh
    # Create a virtual environment (optional but recommended)
    python -m venv venv
    # Activate the virtual environment
    # On Windows
    venv\Scripts\activate
    # On MacOS/Linux
    source venv/bin/activate
    
    # Install the package
    pip install .
    ```
3. Install the Package

    Once you are in your desired environment (virtual or global), 
you can install the `auto_driving_car_simulation` package using pip. 
This will also install all necessary dependencies:

    ```sh
    pip install .
    ```

    This will install the package and create a command-line utility `start-simulation` to run the simulation.


## Usage

To run the simulation, execute the below command:
```sh
start-simulation
```
Follow the on-screen instructions to set up the field, add cars, and run the simulation.

## Running Tests

To run the tests, use pytest:
```sh
python -m pytest    
```
## Project Structure
- src/: Contains the source code for the simulation.
  - auto_driving_car_simulation/
    - main.py: The main entry point for running the simulation.
    - simulation/
      - car.py: Defines the Car class.
      - field.py: Defines the Field class.
      - simulation.py: Defines the Simulation class.
    - localize/
      - localize.py: Handles localization.
      - en.yaml: Contains English localization strings.
    - config/
      - config.py: Contains configuration settings.
    - utils/
      - logger.py: Sets up logging.
- tests/: Contains the test cases for the project.
  - unit/
    - test_car.py: Tests for the Car class.
    - test_field.py: Tests for the Field class.
    - test_simulation.py: Tests for the Simulation class.
  - integration/
    - test_main_integration.py: Integration tests for the main.py functions.
    - test_simulation_integration.py: Integration tests for the Simulation class.
  - e2e/
    - test_e2e_one_car.py: End-to-end tests for single car simulation.
    - test_e2e_two_car_colide.py: End-to-end tests for two car collision simulation.
- setup.py: Script for setting up the package.
- README.md: Project documentation.
- MANIFEST.in: Specifies additional files to include in the package.
- requirements.txt: Lists the dependencies for the project.

## Assumptions
- Application will exit if invalid input provided
- Car name is mandatory and unique
- The car name should be a string and at least one character long.
- Stop moving the car if the new coordinate detected is outside the specified field size or collides with another car