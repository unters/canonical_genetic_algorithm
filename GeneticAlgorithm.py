import random


class GeneticAlgorithm:
    """ Canonical genetic algorithm:
    - chromosome - a binary string,
    - gene       - each bit of binary size,
    - fixed population size,
    - roulette wheel selection,
    - single point crossover,
    - gene-wise mutation """

    POPULATION_SIZE = 20
    POPULATION_LIMIT = 100
    MUTATION_PROBABILITY = 0.15
    RANDOM_SEED = 1979

    # Keep starting population to compare with the resulting population
    starting_population = list()
    resulting_population = list()

    def __init__(self):
        random.seed(self.RANDOM_SEED)
        self.create_starting_population()

        for i in range(self.POPULATION_LIMIT):
            self.panmixia_selection()
            self.population_crossover()
            self.mutate_population()
            self.create_new_population()

    def __str__(self):
        pass

    # Population initialization functions

    def create_individual(self):
        """ Each individual consists of two chromosomes,
        each chromosome is 1 byte long: 4 bits for integer part
        and 4 bits for fractional part """
        x = random.randint(-255, 255)
        y = random.randint(-255, 255)
        individual = [x, y]
        return individual

    def create_starting_population(self):
        for i in range(self.POPULATION_SIZE):
            self.starting_population.append(self.create_individual())

        # Creating a copy of a starting population to work with it
        self.resulting_population = self.starting_population.copy()

    # Selection and breeding functions

    def panmixia_selection(self):
        """ Select individuals for breeding """
        first_parent = random.randint(0, self.POPULATION_SIZE-1)
        second_parent = random.randint(0, self.POPULATION_SIZE - 1)
        breeding_pair = [first_parent, second_parent]
        return breeding_pair

    def single_point_crossover(self, breeding_pair):
        """ Two individuals crossover """
        first_parent = bin(breeding_pair[0])
        second_parent = bin(breeding_pair[1])
        crossover_point = random.randint(0, 7)
        # first_offspring =
        # second_offspring =

    def population_crossover(self):
        """ Proceed crossover for all selected individuals """
        for i in range(self.POPULATION_SIZE):
            breeding_pair = self.panmixia_selection()
            offspring = self.single_point_crossover(breeding_pair)

    # Mutation functions

    def mutate_individual(self):
        pass

    def mutate_population(self):
        pass

    # Selection to new population functions

    def create_new_population(self):
        """ Roulette wheel selection """
        pass
