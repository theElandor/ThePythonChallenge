filename = 'prova.txt'
with open(filename) as file:
    for line in file:
        for ch in line:
            print("Hi")


