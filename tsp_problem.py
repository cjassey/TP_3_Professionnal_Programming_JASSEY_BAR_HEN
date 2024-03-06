# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(GA solving TSP example)
"""
from ga_solver import GAProblem
import cities
import random

class TSProblem(GAProblem):
    """Implementation of GAProblem for the traveling salesperson problem"""
    def _init_(self):
        return super()._init_()
    
    def generate(self):
        "Genreate a new chromosome"
        chromosome = cities.default_road(city_dict)
        random.shuffle(chromosome)
        return chromosome
    
    def score(self, chromosome):
        "Get the fitness for a chromosome"
        fitness = - cities.road_length(city_dict, chromosome)
        return fitness
    
    def reproduction(self, parent_a, parent_b, x_point):
        "Create a new chromosome from 2 parents in the population"
        a_chromosome = parent_a.chromosome[0:x_point]
        b_chromosome = parent_b.chromosome[x_point:]
        cities_to_delete = []
        for k in range(len(a_chromosome)):
            if a_chromosome[k] in b_chromosome :
                cities_to_delete.append(a_chromosome[k])

        for element in cities_to_delete:
            if element in a_chromosome:
                a_chromosome.remove(element)
   
        new_chrom = a_chromosome+b_chromosome
        all_cities = cities.default_road(city_dict)
        for j in range(len(all_cities)):
            if all_cities[j] not in new_chrom :
                new_chrom.append(all_cities[j])
        
        cities_to_delete.clear()
        return new_chrom
    
    def mutation(self, new_chrom):
        "Swap 2 cities in a chromosome "
        ran_a = random.randint(0,len(new_chrom)-1)
        ran_b = random.randint(0,len(new_chrom)-1)
        while ran_b == ran_a:
            ran_b = random.randint(0,len(new_chrom)-1)
        new_chrom[ran_a], new_chrom[ran_b]= new_chrom[ran_b], new_chrom[ran_a]
        return new_chrom

    def get_threshold_fitness(self):
        "For this problem there is no best score to solve it so the treshold fitness is unreachable "
        threshold_fitness=0
        return threshold_fitness

if __name__ == '__main__':

    from ga_solver import GASolver

    city_dict = cities.load_cities("C:\\Users\\cleme\\OneDrive - Fondation EPF\\4A\\Professional Programming\\TP 3\\genetic_part3\\cities.txt")
    problem = TSProblem()
    solver = GASolver(problem)
    solver.reset_population()
    solver.evolve_until()
    cities.draw_cities(city_dict, solver.get_best_individual().chromosome)
