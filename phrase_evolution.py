import random
import string
from time import sleep

PHRASE = "hatz gionule"

# An individual is a phrase
# A population is a bunch of phrases

GENESET = string.ascii_letters + " "
POPULATION_SIZE = 100
MUTATION_RATE = 0.3

def generate_individual():
    length = len(PHRASE)
    return ''.join(random.choice(GENESET) for i in range(length))

def generate_population():
    population = []
    for _ in range(POPULATION_SIZE):
        individual = generate_individual()
        population.append(individual)
    return population

def calculate_fitness(s):
    assert len(s) == len(PHRASE), "Lengths differ."
    return sum(s[i] == PHRASE[i] for i in range(len(s)))

def crossover(population):
    pairs = []
    
    for i in range(len(population)):
        pairs.append((population[i], calculate_fitness(population[i]), i))
    pairs.sort(key = lambda x: x[1], reverse=True)

    p1, p2 = pairs[0][0], pairs[1][0]
    print(p1 + " -- " + str(pairs[0][1]))

    if pairs[0][1] == len(PHRASE):
        print("End.")
        exit(0)

    mating_point = random.randint(0, len(p1))

    child1 = p1[:mating_point] + p2[mating_point:]
    child2 = p2[:mating_point] + p1[mating_point:]

    if random.random() < MUTATION_RATE:
        child1 = mutate(child1)
        child2 = mutate(child2)

    population.append(child1)
    population.append(child2)

    # Remove worst people
    worst_idx1 = pairs[-1][2]
    worst_idx2 = pairs[-2][2]
    del population[worst_idx1]
    del population[worst_idx2]

def mutate(s):
    mutation_point = random.randint(0, len(s))
    letter = random.choice(GENESET)
    new_s = []
    for i in range(len(s)):
        if i == mutation_point:
            new_s.append(letter)
        else:
            new_s.append(s[i])
    return ''.join(new_s)

if __name__ == "__main__":
    population = generate_population()
    generation = 0
    while True:
        generation += 1
        print("Generation: " + str(generation))
        crossover(population)