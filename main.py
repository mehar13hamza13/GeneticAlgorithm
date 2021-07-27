import random




class GeneticAlgo:

    def __init__(self, population_size, mutation_rate):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        # filling in the random numbers from 0 to 31 at start
        self.population = random.sample(range(0, 31),population_size)
        self.pool = []


    def fitness_function(self):
        self.pool = []
        fittest_element = 0
        fitness_index = 0
        # fitness function : f(x) = x^2
        for i in range(self.population_size):
            if(self.population[i]**2 > fittest_element**2):
                fittest_element = self.population[i]
                fitness_index = i

            temp = [self.population[i]]*(self.population[i]**2) # appending x^2 times the attribute into the pool
            self.pool  = self.pool + temp

        return fittest_element, fitness_index



    def crossover(self, parent1, parent2):
        parent1 = str(bin(parent1))[2:]
        parent2 = str(bin(parent2))[2:]

        # converting the decimal numbers into binary to perform crossover
        #crossover technqiue used : one
        child = ""
        for i in range(len(parent1)):
            if(i < len(parent1)/2):
                child = child + parent2[i]
            else:
                child = child + parent1[i]

        child = self.mutation(child) #mutating the child
        child  = int(child, 2)

        return child

    def mutation(self, element):
        for i in range(len(element)):
            if(random.random() < self.mutation_rate):
                # flips the bit
                if element[i] == "0":
                    element = element[:i] + "1" + element[i + 1:]
                else:
                    element = element[:i] + "0" + element[i + 1:]

        return element

    def calculate_avg(self):
        avg = sum(self.population) / self.population_size
        return avg

    def selection(self):
        fittest_element, fitness_index = self.fitness_function()
        print("Fittest element: "+str(fittest_element)+", index: "+str(fitness_index))
        for i in range(len(self.population)):
            parent1 = self.pool[random.randrange(0, len(self.pool))]
            parent2 = self.pool[random.randrange(0, len(self.pool))]
            self.population[i] = self.crossover(parent1=parent1, parent2=parent2)


    def run(self):
        generation = 1
        print("Average of Population: " + str(self.calculate_avg()))
        print("Population : ", end="")
        print(self.population)

        while self.calculate_avg() <= 29:
            print("Generation: "+ str(generation))
            self.selection()
            print("Population : ", end="")
            print(self.population)
            print("Average of Population: " + str(self.calculate_avg()))
            generation += 1


ga = GeneticAlgo(8, 0.05)
ga.run()


