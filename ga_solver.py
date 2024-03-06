# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(generic genetic algorithm module)
"""
import random

class Individual:
    """Represents an Individual for a genetic algorithm"""

    def __init__(self, chromosome: list, fitness: float):
        """Initializes an Individual for a genetic algorithm

        Args:
            chromosome (list[]): a list representing the individual's
            chromosome
            fitness (float): the individual's fitness (the higher the value,
            the better the fitness)
        """
        self.chromosome = chromosome
        self.fitness = fitness

    def __lt__(self, other):
        """Implementation of the less_than comparator operator"""
        return self.fitness < other.fitness

    def __repr__(self):
        """Representation of the object for print calls"""
        return f'Indiv({self.fitness:.1f},{self.chromosome})'


class GAProblem:
    """Defines a Genetic algorithm problem to be solved by ga_solver"""
    def _init_(self):
        pass

    def generate(self):
        "Generate a chromosome"
        pass

    def score(self, chromosome):
        "Get the fitness for a chromosome given"
        pass

    def reproduction(self, parent_a, parent_b, x_point):
        "Create a new chromosome from 2 parent"
        pass

    def mutation(self, new_chrom):
        "Modify a new chromosome"
        pass

    def get_threshold_fitness():
        "Get the fitness we want to solve the problem"
        pass

class GASolver:
    def __init__(self, problem: GAProblem, selection_rate=0.5, mutation_rate=0.1):
        """Initializes an instance of a ga_solver for a given GAProblem

        Args:
            problem (GAProblem): GAProblem to be solved by this ga_solver
            selection_rate (float, optional): Selection rate between 0 and 1.0. Defaults to 0.5.
            mutation_rate (float, optional): mutation_rate between 0 and 1.0. Defaults to 0.1.
        """
        self._problem = problem
        self._selection_rate = selection_rate
        self._mutation_rate = mutation_rate
        self._population = []

    def reset_population(self, pop_size=50):
        """ Initialize the population with pop_size random Individuals """
        for i in range(pop_size) : 
            chromosome = self._problem.generate()
            fitness = self._problem.score(chromosome)
            new_individual = Individual(chromosome, fitness)
            self._population.append(new_individual)
    
    def evolve_for_one_generation(self):
        """ Apply the process for one generation : 
            -	Sort the population (Descending order)
            -	Selection: Remove x% of population (less adapted)
            -   Reproduction: Recreate the same quantity by crossing the 
                surviving ones 
            -	Mutation: For each new Individual, mutate with probability 
                mutation_rate i.e., mutate it if a random value is below   
                mutation_rate
        """
        #Selection
        self._population.sort(reverse=True)
        size = len(self._population)
        size_by_selected_rate = int(size*self._selection_rate)
        self._population = self._population[0:int(size_by_selected_rate)]

        #Reproduction
        for i in range(size_by_selected_rate):
            a = random.randrange(0, size_by_selected_rate)
            b = random.randrange(0, size_by_selected_rate)
            if len(set(self._population)) > 1 : # Check if there is at least 2 unique individuals in the population to get 2 different parents for the reproduction
                while a == b : 
                    b = random.randrange(0, size_by_selected_rate)
            parent_a = self._population[a]
            parent_b = self._population[b]
            x_point = random.randrange(0, len(self._population[0].chromosome)) 
            
            new_chrom = self._problem.reproduction(parent_a,parent_b,x_point)
            new_fitness = self._problem.score(new_chrom)

        #Mutation
            number = random.random()
            if number < self._mutation_rate :
                new_chrom = self._problem.mutation(new_chrom)
                new_fitness = self._problem.score(new_chrom)
        
            new_individual = Individual(new_chrom, new_fitness)
            self._population.append(new_individual)



    def show_generation_summary(self):
        """ Print some debug information on the current state of the population """
        pass  # REPLACE WITH YOUR CODE
    

    def get_best_individual(self):
        """ Return the best Individual of the population """
        self._population.sort(reverse=True)
        return self._population[0]

    def evolve_until(self, max_nb_of_generations=500, threshold_fitness=None):
        """ Launch the evolve_for_one_generation function until one of the two condition is achieved : 
            - Max nb of generation is achieved
            - The fitness of the best Individual is greater than or equal to
              threshold_fitness
        """
        for i in range(max_nb_of_generations):
            self.evolve_for_one_generation()
            best_ind = self.get_best_individual()
            threshold_fitness = self._problem.get_threshold_fitness()
            if best_ind.fitness >= threshold_fitness:
                print("nombre de génération : ", i)
                break
