import random
n=random.randrange(20,50)
m=[[0 for col in range(n)] for row in range(n)]
h = random.sample(range(1, n), n-1)

for i in range(n):
    if i < n-2:
        m[h[i-1]][h[i]] = 1
        m[h[i]][h[i-1]] = 1
    else:
        m[h[i-1]][h[0]] = 1
        m[h[0]][h[i-1]] = 1

lista=[]
for i in range(n):
    for j in range(n):
        if m[i][j]==1:
            lista.append([i,j])
f=open('gc.txt', 'w')
f.write('%s\n' % n)
for i in range(n):
		f.write('%d %d \n' %(lista[i][0] ,lista[i][1]))

f = open('gc.txt', 'r')
#print(f.read())

with open('inst.txt', 'r') as f:
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
    #wypisać ilość kolorow
  return tab

tab= KolorujZachlannie(arr)

print("Węzeł\tKolor")

def checkValidity(chromosome, parentLen ):
    # check just adjacent colors
    isValid = True
    for i in range(0, parentLen):
        if (chromosome[i] == chromosome[(i+1)%parentLen]):
            isValid = False
            break
    return isValid

# for i in range(0, w):
#   print(str(i+1) + "\t" + str(tab[i]+1))
# print(max(tab)+1)
print(tab)


# mutate child
def mutate(child): 
    for i in range(0, len(child)):
        if random.random() < 0.5:
            child[i] = random.randrange(0, w)
    return child

def cross(parent1, parent2):
        child = []
        for i in range(0, len(parent1)):
            if random.random() < 0.5:
                child.append(parent1[i])
            else:
                child.append(parent2[i])
        if random.random() < 0.5:
          child = mutate(child)
          return child
        else:
          return child
# cross funciton with mutation


def fitness(chromosome):
        fitness = 0
        for i in range(0, w):
            for j in range(i+1, w):
                if (chromosome[i] == chromosome[j]):
                    fitness += 1
        return fitness




def genetic(greedy_solution, number_of_generations, population_size):
    # make population
    for generation in range(0, number_of_generations):
      population = []
      parentlen = len(greedy_solution)
      population.append(greedy_solution)
      maxcolor=max(tab)
      for i in range(0, population_size):
          population.append([random.randrange(0, maxcolor) for i in range(0, parentlen)])
      
      # cross population
      for i in range(0,population_size):
          population.append(cross(population[i], population[i+1]))
      # # reduce population
      for i in range(0, 100): 
          population[i] = [fitness(population[i]), population[i]]
          #population.sort() 
      # population.sort()
     # filter population\
      population = filter(lambda x: checkValidity(x, parentlen), population)
      # remove worst
      #population = population[0:50]
      # print best

      # print("Generation: " + str(generation) + " Best: " + str(population[0][0]))       
      [print(element, checkValidity(element,parentlen)) for element in population]
      # print()

genetic(tab,1,10)
  
    









