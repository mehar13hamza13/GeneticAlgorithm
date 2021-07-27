import random




class GeneticAlgorithm:

    def __init__(self):
        self.pop_size = 6
        self.mutation_rate = 0.05

        # getting random numbers from 0 to 30
        self.data = []
        # filling the population with random numbers one by one
        for i in range(self.pop_size):
            self.data.append(random.randrange(0, 31))

        # list for pooling
        self.poollist = []



    def mutate(self, obj):
        for i in range(len(obj)):
            if(random.random() < self.mutation_rate):
                # flipping the bit (0.05% chance)
                obj = obj[:i] + str(abs(int(obj[i])-1)) + obj[i + 1:]

        return obj



    def crossover(self, father, mother):
        father = str(bin(father))[2:]
        mother = str(bin(mother))[2:]

        children = ""

        #crossing over half elements

        for i in range(len(father)):
            if (i < len(father) / 2):
                children = children + mother[i]
            else:
                children = children + father[i]

        children = self.mutate(children)
        children = int(children, 2)

        return children





    def check_fitness(self):
        self.poollist = []
        fit_num = 0
        index = 0

        # applying the fitness function
        for i in range(self.pop_size):
            if self.data[i]**2 > fit_num**2:
                fit_num = self.data[i]
                index = i
            # adding items to the pool
            a = [self.data[i]] * int((self.data[i] ** 2)/self.pop_size)
            self.poollist = self.poollist + a

        return (fit_num, index)


    def avg(self):
        average = sum(self.data) / self.pop_size
        return average

    def select_gen(self, j):
        fitlist = self.check_fitness()

        print("Most fit individual: " + str(fitlist[0]) + ", index in list: " + str(fitlist[1]))
        for i in range(len(self.data)):
            # selecting random mother and father from the pool list
            father = self.poollist[random.randrange(0, len(self.poollist))]
            mother = self.poollist[random.randrange(0, len(self.poollist))]
            self.data[i] = self.crossover(father=father, mother=mother)
            if(j == 1):
                print("Father: ", end="")
                print(father)
                print("Mother: ", end="")
                print(mother)


    def iterate(self):
        generation_num = 1

        print("-----Generation Average:" + str(self.avg()))
        print("Population : ", end="")
        print(self.data)
        print()

        while self.avg() <= 29:
            print("---------Generation Number: " + str(generation_num))
            self.select_gen(generation_num)
            print("Population : ", end="")
            print(self.data)
            print("-----Generation Average: " + str(self.avg()))
            generation_num += 1
            print()


if __name__ == "__main__":
    obj = GeneticAlgorithm()
    obj.iterate()