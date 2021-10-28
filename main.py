from GeneticAlgorithm import GeneticAlgorithm
from functions import RosenbrockFunction
from functions import HimmelblauFunction
from functions import SphereFunction


def main():
    # sf = SphereFunction()
    # function = sf.function

    rf = RosenbrockFunction()
    function = rf.function

    # hf = HimmelblauFunction()
    # function = hf.function

    # sf.draw_plot()
    # rf.draw_plot()
    # hf.draw_plot()

    ga = GeneticAlgorithm(function)

    starting_population = list()
    resulting_population = list()
    for individual in ga.starting_population:
        starting_population.append(
            [individual[0].get_float_representation(),
             individual[1].get_float_representation()])

    for individual in ga.resulting_population:
        resulting_population.append(
            [individual[0].get_float_representation(),
             individual[1].get_float_representation()])

    # sf.draw_plot(starting_population, resulting_population)
    rf.draw_plot(starting_population, resulting_population)
    # hf.draw_plot(starting_population, resulting_population)

    # for i in range(ga.POPULATION_SIZE):
    #     print(round(ga.starting_population[i][0], 2),
    #           round(ga.starting_population[i][1], 2), "\t",
    #           round(ga.resulting_population[i][0], 2),
    #           round(ga.resulting_population[i][1], 2), end='\n')


if __name__ == "__main__":
    main()
