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

with open('queen6.txt', 'r') as f:
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

def get_all_adjecent_colors(colorIndex,chromosome):
  colors = []
  for j in range(0, len(macierz)):
    if macierz[colorIndex][j] == 1 and colorIndex != j:
      colors.append(chromosome[j])
  return colors


def checkValidity2(chromosome):
    # check just adjacent colors
    # isValid = True
    chromosomeBeforeErrror = chromosome
    error_list=[]
    # check if adjacent matrix nodes are the same color
    for i in range(0, len(chromosome)):
        for j in range(i, len(chromosome)):
            if (macierz[i][j] == 1 and chromosome[i] == chromosome[j]):
                error_list.append(j)
    for error in error_list:
      color_list = get_all_adjecent_colors(error,chromosome)
      all_possible_colors = list(range(0,max(chromosome)))
      # list difference
      if(len(set(all_possible_colors) - set(color_list)) > 0):
        color = min(list(set(all_possible_colors) - set(color_list))) 
      else:
        color = max(color_list) + 1
      chromosome[error] = color
      
    return chromosome
    # return 
    # Tak ot my majemo cej wierzholek bledny lista-koloriv [1,3,7] vsi kolory [1,2,3,4,5,6,7]

  
def checkValidity(chromosome, parentLen ):
    # check just adjacent colors
    isValid = True
    # check if adjacent matrix nodes are the same color
    for i in range(0, parentLen):
        for j in range(i, parentLen):
            if (macierz[i][j] == 1 and chromosome[i] == chromosome[j]):
                isValid = False
    return isValid

# for i in range(0, w):
#   print(str(i+1) + "\t" + str(tab[i]+1))
print("Greedy solution", max(tab)+1)
# print(tab)
    # def szukanie_bledow(self):
    #     lista_bledow = []
    #     slownik_bledow = {}
    #     lista_posortowanych = []
    #     for x in range(len(self.macierz)):
    #         for y in range(len(self.macierz)):
    #             if self.macierz[x][y]:
    #                 if (x+1 in lista_bledow or y+1 in lista_bledow):
    #                     continue
    #                 if (self.slownik_kolorow[x+1] == self.slownik_kolorow[y+1]):
    #                     lista_bledow.append(y+1)

    #     index = 0

    #     for i in range(len(lista_bledow)):
    #         naprawa = self.kolorowanie_jednego(lista_bledow[index],False)
    #         # (lista_bledow[index],index,i)
    #         if naprawa:
    #             lista_bledow.remove(lista_bledow[index])
    #         else:
    #             index+=1

    #     for kolor in lista_bledow:
    #         ilosc_sasiadow = 0
    #         for i in range(len(self.macierz)):
    #             if self.macierz[kolor-1][i]:
    #                 ilosc_sasiadow+=1
    #         slownik_bledow[kolor]=ilosc_sasiadow

    #     posortowane_wierzcholki = sorted(slownik_bledow.items(), key=lambda x: x[1], reverse=True)
    #     for x in posortowane_wierzcholki:
    #         lista_posortowanych.append(x[0])

    #     #lista_bledow.sort()
    #     if lista_posortowanych == None:
    #         self.lista_bledow = []
    #     else:
    #         self.lista_bledow = lista_posortowanych

    # def error_correcting(self):
    #         #self.lista_bledow = self.szukanie_bledow()
    #         #print("lista_bledow przed error_correcting", self.lista_bledow)
    #         for i in range(len(self.lista_bledow)):
    #             self.kolorowanie_jednego(self.lista_bledow[0],True)
    #             #print ("usuwam wierzcholek",self.lista_bledow[0]," z listy bledow",self.lista_bledow)
    #             self.lista_bledow.remove(self.lista_bledow[0])
    #         #print("lista_bledow po error_correcting", self.lista_bledow)


# mutate child
def mutate(child): 
    firstIdex = random.randint(0,len(child)-1)
    # second index to be different from first index
    secondIndex = random.randint(0,len(child)-1)
    while secondIndex == firstIdex:
        secondIndex = random.randint(0,len(child)-1)
    child[firstIdex], child[secondIndex] = child[secondIndex], child[firstIdex]
    # for i in range(0, len(child)):
    #     if random.random() < 0.5:
    #         child[i] = random.randrange(0, max(tab))
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

# compare two lists with number of errors
def compare(list1, list2):
  count = 0
  for i in range(0, len(list1)):
    if list1[i] != list2[i]:
      count += 1
  return count
   


def genetic(greedy_solution, number_of_generations, population_size, mutation_rate):
    # make population
  population = []
  parentlen = len(greedy_solution)
  # population.append(greedy_solution)
  maxcolor=max(tab)

  for generation in range(0, number_of_generations):
      for i in range(0, population_size//3):
          listinplace = list(range(parentlen))
          random.shuffle(listinplace)
          population.append(listinplace)
      # cross population
      for i in range(0,population_size):
          population.append(cross(population[i], population[i+1], mutation_rate))
      # # reduce population
    
      # fix check validity !!!
      # remove duplicates from list of lists
      # compare two lists python
    


      # population = list(filter(lambda x: checkValidity(x, parentlen), population))
      population = list(filter(lambda x: checkValidity2(x), population))
      # print(population[0])
      # population = list(filter(lambda x: fitness(x) <= max(tab), population))
      # sort by fist element in array
      population = sorted(population, key=fitness)
      # population = list(filter(lambda x: compare(x, population[0]) < 5, population[1:]))

      # remove similar elements
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
         print("Generation: " + str(generation) + " Best: " + str(str(population[0][0:10]) +  str(fitness(population[0])+1)) )      
         print("Generation: " + str(generation) + " Best: " + str(str(population[1][0:10]) + str(fitness(population[1])+1)) )      
         print("Generation: " + str(generation) + " Best: " + str(str(population[2][0:10]) + str(fitness(population[2])+1)) )      
      print("g" + str(generation))

      population = population[:population_size]
      # [print(element[1], element[0]) for element in population[0:10]]
      # print("Generation: " + str(generation) + " Best: " + str(population[0][0]+1))       
      # print()

# genetic(tab,1,20,1)
genetic(greedy_solution = tab, number_of_generations = 200, population_size=50, mutation_rate=1)
  
    









