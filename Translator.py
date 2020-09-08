## if vocale ---> yay alla fine
## if consonante ---> prima lettera alla fine + ay

def translate(sentence):
    vowels = ['a' , 'e' , 'i' , 'o', 'u', 'A', 'E',"I","O","U"]
    list = sentence.split()
    print(list)
    for i in range(len(list)):
        if list[i].isalpha() == True:
            if list[i][0] in vowels:
                list[i] += 'yay'
            else:
                to_replace = list[i][0]
                list[i] = list[i].replace(to_replace, "",1)
                list[i] += to_replace + "ay"

    separator = " "
    print(separator.join(list))

x = input("Inserisci una frase\n")
translate(x)
