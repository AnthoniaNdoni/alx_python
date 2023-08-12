# Almost a Circle

Welcome to the "Almost a Circle" project! This project implements a Python package that contains classes for managing geometric shapes, with a focus on circles.

## Project Structure

The project is organized into the following directory structure:
almost_a_circle/
├── models/
│ ├── init.py
│ └── base.py
├── README.md
└── main.py

- The `models` directory contains the core classes for managing geometric shapes.
- The `base.py` file defines the `Base` class, which serves as the foundation for managing attributes like the id across different classes.
- The `main.py` file is a sample usage demonstration of the classes defined in the `models` package.

## `Base` Class

The `Base` class is the base for all other classes in this project. It manages the id attribute to ensure unique identifiers for instances. It includes:
- A private class attribute `__nb_object` to keep track of instance count.
- A constructor `__init__` to initialize instances with unique ids.

## Getting Started

To use the project, you can:
1. Clone this repository.
2. Navigate to the `almost_a_circle` directory.
3. Run the `main.py` file to see the sample usage and demonstrations.

Documentation
Detailed documentation for the classes and their methods can be found in the respective source files.

Contributions
Contributions, bug reports, and suggestions are welcome! Feel free to submit issues and pull requests to improve the project.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Author: Anthonia Ndoni