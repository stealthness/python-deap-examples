"""
This file contains the items used in knapsack problem.
Each item has description, weight and value.
"""
bag_items = (
    ("map", 9, 150),
    ("compass", 13, 35),
    ("water", 153, 200),
    ("sandwich", 50, 160),
    ("glucose", 15, 60),
    ("tin", 68, 45),
    ("banana", 27, 60),
    ("apple", 39, 40),
    ("cheese", 23, 30),
    ("beer", 52, 10),
    ("suntan cream", 11, 70),
    ("camera", 32, 30),
    ("t-shirt", 24, 15),
    ("trousers", 48, 10),
    ("umbrella", 73, 40),
    ("waterproof trousers", 42, 70),
    ("waterproof overclothes", 43, 75),
    ("note-case", 22, 80),
    ("sunglasses", 7, 20),
    ("towel", 18, 12),
    ("socks", 4, 50),
    ("book", 30, 10),
    )


def printBag(geno):
    bag = []
    for idx, gene in enumerate(geno):
        print(gene,idx)
        if gene == 1:
            bag.append(bag_items[idx])
            print(f'adding {bag_items[idx][0]}, with weight {bag_items[idx][1]}, and value of {bag_items[idx][2]}')

print('start')
printBag([1, 1, 0])