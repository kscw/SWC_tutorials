def read_animals(filestring):
    f = open(filestring,'r')
    date = []
    time = []
    animal = []
    number = []
    for line in f:
        d, t, a, n = line.split()
        date.append(d)
        time.append(t)
        animal.append(a)
        number.append(int(n))
    return date, time, animal, number    

def mean(l):
    """
    returns the mean value from a list
    """
    s = 0;
    for x in l:
        s = s + x 
    return float(s)/len(l)

def get_animal(date,time, animal, number , animal_name):
    new_date = []
    new_time = []
    new_number = []
    for d, t, a, n in zip(date, time, animal, number):
        if a == animal_name:
            new_date.append(d)
            new_time.append(t)
            new_number.append(n)
    return new_date, new_time, new_number


    #for i in range(len(animal)):
    #    if animal_name == animal[i]:
    #          sum = sum+number[i] 
    return sum

#date, time, animal, number = read_animals('animals.txt')
#grizzlyno = get_animal(date,time,animal,number,'Grizzly')
#print grizzlyno
def main(filename, animalname):
    date,time,animal,number = read_animals(filename)    
    date,time,number = get_animal(date,time,animal, number,animalname)
    mnumber = mean(number)
    return mnumber

