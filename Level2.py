from pprint import pprint
text = open('prova.txt').read()
char_frequency = {}
lista = []
for char in text:
    if char in char_frequency:
        char_frequency[char] +=1
    else:
        char_frequency[char] = 1
pprint(char_frequency,width = 1)

for element in char_frequency.items():
    lista.append(element)
print(lista)