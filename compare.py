from datetime import datetime

def compare(file_path, file_path_b):
    print(datetime.now())
    lista_a = open(file_path, 'r').read().split('\n')
    lista_b = open(file_path_b, 'r').read().split('\n')
    conjunto_a = set(lista_a)    
    conjunto_b = set(lista_b)
    # difference = conjunto_a.difference(conjunto_b)
    intersection = conjunto_a.difference(conjunto_b)
    print(len(intersection))
    print(datetime.now())

def compare2():
    print(datetime.now())
    count = 0
    names_a = open('names_a.txt', 'r').read().split('\n')
    names_b = open('names_b.txt', 'r').read().split('\n')
    intersection = []
    for name in names_a:
        count += 1
        if name in names_b:
            intersection.append(name)
        if count == 1000:
            print(datetime.now())    
    print(len(intersection))


if __name__ == "__main__":
    #compare2()
    compare('random_string.txt', 'random_string_b.txt')

