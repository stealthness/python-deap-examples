"""
The purpose of this this scrpit is set of utility functions
"""


def get_top_individual(pop: list, n: int = 3):
    """Returns the top n individuals in a population, default is the top three"""
    pop.sort(reverse=True)
    return pop[0:3]
