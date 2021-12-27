import math
import random
# # n=random.randrange(20,50)
# n=10
# m=[[0 for col in range(n)] for row in range(n)]
# h = random.sample(range(1, n), n-1)

# for i in range(n):
#     if i < n-2:
#         m[h[i-1]][h[i]] = 1
#         m[h[i]][h[i-1]] = 1
#     else:
#         m[h[i-1]][h[0]] = 1
#         m[h[0]][h[i-1]] = 1

# lista=[]
# for i in range(n):
#     for j in range(n):
#         if m[i][j]==1:
#             lista.append([i,j])
# f=open('gc.txt', 'w')
# f.write('%s\n' % n)
# for i in range(n):
# 		f.write('%d %d \n' %(lista[i][0] ,lista[i][1]))

f = open('gc.txt', 'r')
#print(f.read())

with open('myciel4.txt', 'r') as f:
    w = int(f.readline())
    arr=[[0 for i in range(w)]for j in range(w)]
    #[print(arr[i]) for i in range(w)]
    kr=f.readline().split()
    while kr != []:
        arr[int(kr[0])-1][int(kr[1])-1]=1
        arr[int(kr[1])-1][int(kr[0])-1]=1
        kr=f.readline().split()
    #[print(arr[i]) for i in range(w)]
    
def KolorujZachlannie(macierz):
  n = len(macierz)
  tab = [-1] * n
  tab[0] = 0
  kolory = [False] * n
  for i in range(n):
    for j in range(n):
      kolory[j] = False
    for j in range(n):
      if (macierz[i][j] > 0 and tab[j] != -1):
        kolory[tab[j]] = True
    k = 0
    while kolory[k]:
      k += 1
    tab[i] = k
  # print(macierz)
    #wypisać ilość kolorow
  return tab,macierz

tab,macierz= KolorujZachlannie(arr)

# print("Węzeł\tKolor")
# [print(x) for x in macierz]

def checkValidity(chromosome, parentLen ):
    # check just adjacent colors
    isValid = True
    # check if adjacent matrix nodes are the same color
    for i in range(0, parentLen):
        for j in range(0, parentLen):
            if (macierz[i][j] == 1 and chromosome[i] == chromosome[j]):
                isValid = False
    return isValid

# for i in range(0, w):
#   print(str(i+1) + "\t" + str(tab[i]+1))
print("Greedy solution", max(tab)+1)
# print(tab)


# mutate child
def mutate(child): 
    for i in range(0, len(child)):
        if random.random() < 0.5:
            child[i] = random.randrange(0, max(tab))
    return child


def cross(parent1, parent2, mutation_rate=0.5):
        child = []
        for i in range(0, len(parent1)):
            if random.random() < 0.5:
                child.append(parent1[i])
            else:
                child.append(parent2[i])
        if random.random() < mutation_rate:
          child = mutate(child)
          return child
        else:
          return child
# cross funciton with mutation
def cross2(parent1, parent2, mutation_rate=0.5):
  # crossover two parents to create two children
  child1 = []
  child2 = []
  # split parents by half
  parent1_len = len(parent1)
  parent2_len = len(parent2)
  split = int(parent1_len / 2)
  # crossover
  for i in range(0, split):
    child1.append(parent1[i])
    child2.append(parent2[i])
  for i in range(split, parent1_len):
    child1.append(parent2[i])
    child2.append(parent1[i])
  # mutate children
  if random.random() < mutation_rate:
    child1 = mutate(child1)
  if random.random() < mutation_rate:
    child2 = mutate(child2)
  return child1



def fitness(chromosome):
  return max(chromosome)
        # fitness = 0
        # for i in range(0, w):
        #     for j in range(i+1, w):
        #         if (chromosome[i] == chromosome[j]):
        #             fitness += 1
        # return fitness



def genetic(greedy_solution, number_of_generations, population_size, mutation_rate):
    # make population
  population = []
  parentlen = len(greedy_solution)
  population.append(greedy_solution)
  maxcolor=max(tab)

  

  for generation in range(0, number_of_generations):
      for i in range(0, population_size):
          population.append([random.randrange(0, maxcolor +1 ) for i in range(0, parentlen)])
      # cross population
      for i in range(0,population_size):
          population.append(cross(population[i], population[i+1], mutation_rate))
      # # reduce population
    
      # fix check validity !!!


      population = list(filter(lambda x: checkValidity(x, parentlen), population))
      # print(population[0])
      # population = list(filter(lambda x: fitness(x) <= max(tab), population))
      # sort by fist element in array
      population = sorted(population, key=fitness)
      # for index in range(0, len(population)): 
      #   # print(population[index], fitness(population[index]))
      #   if isinstance(population[index], list):
      #     continue
      #   else:
      #     population[index] = [fitness(population[index]), population[index]]
          #population.sort() 
      
      # population.sort(key=lambda x: x[0])

    #   population.sort()
    #  filter population\
    #   remove worst
    #   population = population[0:population_size]
    #   print best
      if(len(population)> 0):
         print("Generation: " + str(generation) + " Best: " + str(fitness(population[0])+1))       
      print("g" + str(generation))

      population = population[:population_size]
      # [print(element[1], element[0]) for element in population[0:10]]
      # print("Generation: " + str(generation) + " Best: " + str(population[0][0]+1))       
      # print()

# genetic(tab,1,20,1)
genetic(greedy_solution = tab, number_of_generations = 1000, population_size=50, mutation_rate=0.5)
  
    









