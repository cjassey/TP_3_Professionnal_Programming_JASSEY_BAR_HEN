# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(GA solving Mastermind example)
"""
from ga_solver import GAProblem
import mastermind as mm
import random


class MastermindProblem(GAProblem):
    """Implementation of GAProblem for the mastermind problem"""
    def _init_(self):
        return super()._init_()
    
    def generate(self):
        "Generate a chromosome randomly"
        chromosome = match.generate_random_guess()
        return chromosome
    
    def score(self, chromosome):
        "Get the fitness associate with a chromosome"
        fitness = match.rate_guess(chromosome)
        return fitness
    
    def reproduction(self, parent_a, parent_b, x_point):
        "Create a new chromosome from 2 parents in the population"
        new_chrom = parent_a.chromosome[0:x_point] + parent_b.chromosome[x_point:]
        return new_chrom
    
    def mutation(self, new_chrom):
        "Change a color into a chromosome "
        valid_colors = mm.get_possible_colors()
        new_gene = random.choice(valid_colors)
        pos= random.randrange(0, len(new_chrom))
        new_chrom = new_chrom[0:pos] + [new_gene] + new_chrom[pos+1:]
        return new_chrom
    
    def get_threshold_fitness(self):
        "Get the max score for this problem to finsih the programm"
        threshold_fitness=match.max_score()
        return threshold_fitness
    
if __name__ == '__main__':

    from ga_solver import GASolver

    match = mm.MastermindMatch(secret_size=6)
    problem = MastermindProblem()
    solver = GASolver(problem)
    solver.reset_population()
    solver.evolve_until()

    print(
        f"Best guess {solver.get_best_individual()}")
    print(
        f"Problem solved? {match.is_correct(solver.get_best_individual().chromosome)}")


    # {mm.encode_guess(solver.max_score())}