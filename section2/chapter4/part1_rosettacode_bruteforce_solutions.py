"""
This file contains solution from rosetta code that brute force the knapsack problem

http://rosettacode.org/wiki/Knapsack_problem/0-1
"""
import timeit
# begin
from section2.chapter4.bag_data import bag_items

tic = timeit.default_timer()

MAX_WEIGHT = 400


def total_value(items, max_weight):
    return sum([x[2] for x in items]) if sum([x[1] for x in items]) <= max_weight else 0


cache = {}


def solve(items, max_weight):
    if not items:
        return ()
    if (items, max_weight) not in cache:
        head = items[0]
        tail = items[1:]
        include = (head,) + solve(tail, max_weight - head[1])
        dont_include = solve(tail, max_weight)
        if total_value(include, max_weight) > total_value(dont_include, max_weight):
            answer = include
        else:
            answer = dont_include
        cache[(items, max_weight)] = answer
    return cache[(items, max_weight)]


solution = solve(bag_items, MAX_WEIGHT)



# end
toc = timeit.default_timer()

print(f'time passed was {toc - tic}')
