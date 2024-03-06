# What is a GA problem

We talk of Genetic Algorithms to describe an algorithmic design pattern where the potential solutions to a problem are seen as a population and where we seek the most 
adapted individuals of this population put under a Darwinist selective pressure (only themost adapted survive and reproduce). 
In the end, the most adapted individual is considered the best solution to the problem.

# Genetic Algorithm Module

This module implements a generic genetic algorithm for solving optimization problems. It provides classes and methods for defining and solving problems using a genetic algorithm.

## Installation

No specific installation is required. This module is a autonomous Python file that can be imported into your existing Python project.

## Use

1. **Define a problem**: To use this algorithm, you need to define a specific problem by creating a class which inherits from the `GAProblem` class. This class must implement the following methods: `generate`, `score`, `reproduction`, `mutation` and `get_threshold_fitness`.

2. **Create an instance of the solver**: Once you have defined your problem, you can create an instance of the `GASolver` class, passing the problem as an argument.

3. **Initialise the population**: Use the `reset_population` method to initialise the population with random individuals.

4. **Evolve population**: Use the `evolve_for_one_generation` method to evolve the population for one generation.
     ***Selection***
        It is the step when you choose the best individuals in the population. The number of individuals selected is initilaze in the def : "_init_"
    ***Reproduction***
        It is the step when you recreate indivduals from parents already existing in the population to replace the individuals dropped during the selection.
    ***Mutation***
        It is the step when you change randomly a gene ( a part of a chromosome ) after the reproduction step.

5. **Check convergence**: Use the `evolve_until` method to evolve the population until a stopping criterion is reached, such as a maximum number of generations or a fitness threshold. However, depending on the problem, the stopping criterion is not mandatory.

6.**Get the best individual**: Use the `get_best_individual` method to get the best individual from the current population based on the fitness of each individual.


## Example of use

```python
from genetic_algorithm import GAProblem, GASolver

# Define your specific problem
class MyProblem(GAProblem):
    # Implement the necessary methods here

# Create an instance of the solver
problem = MyProblem()
solver = GASolver(problem)

# Initialise the population
solver.reset_population()

# Evolve the population until it converges
solver.evolve_until()

# Obtain the best individual
best_individual = solver.get_best_individual()
print("Best individual:", best_individual)

```
## Example of utilisation already in this module

>'tsp_problem.py
>'mastermind_problem.py

