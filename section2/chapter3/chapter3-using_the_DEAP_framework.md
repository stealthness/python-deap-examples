#  Chapter 3 - Using the DEAP Framework

## Source Material

Note selected Notes taken from "Hands-On Genetic Algorithms with Python" Copyright © 2020 Packt Publishing.3

DEAP (short for Distributed Evolutionary Algorithms in Python) is a Python framework that supports the rapid
development of solutions using genetic algorithms, as well as other evolutionary computation techniques. DEAP offers
various data structures and tools that prove essential when implementing a wide range of genetic algorithm-based
solutions.DEAP was developed at the Canadian Laval University in 2009 and is available under the GNU Lesser General
Public License (LGPL).

The source code for DEAP is available at https://github.com/DEAP/deap and the documentation can be found at
https://deap.readthedocs.io/en/master/.

## The _creator_ Module

The _creator_ module is used as a meta-factory

## The _tools_ Module

the tools modules contains useful functions

#### Selection Functions

* selRoulette() -- implements wheel selection
* selStochasticUniversalSampling() implements Stochastic Universal Sampling (SUS).
* selTournament() implements tournament selection.

#### Crossover functions
Crossover functions can be found in the crossover.py file:

* cxOnePoint() implements single-point crossover.
* cxUniform() implements uniform crossover.
* cxOrdered() implements ordered crossover (OX1).
* cxPartialyMatched() implements partially matched crossover (PMX).

#### Mutation Functions

A couple of the Mutation functions that can be found in the mutation.py file are as follows:

* mutFlipBit() implements flip bit mutation.
* mutGaussian() implements normally distributed mutation.

## The One Max Problem

The OneMax (or One-Max) problem is a simple optimization task that is often used as the Hello World of genetic algorithm
frameworks. We will use this problem for the rest of this chapter to demonstrate how DEAP can be used to implement a
genetic algorithm.

The OneMax task is to find the binary string of a given length that maximizes the sum of its digits.