
##1 caricare correttamente il tutto
def converti(arr):
    for i in range(len(arr)):
        arr[i] = int(arr[i])
def print_arr(arr):
    for x in arr:
        print(x, end =' ')
    print('\n')

def print_inc(arrs , dict):
    print("Stampo solo i vettori ordinati in ordine crescente.")
    for x in range (1,len(arrs)+1): ## <= len(arr)
        i = 0
        inc = False
        while(i < len(arrs[x-1])-1 and inc == False):
            if(arrs[x-1][i] > arrs[x-1][i+1]):
                inc = True
            i = i+1
        if(inc == False):
            print_arr(arrs[x-1])
        else:
            inc = False
f = open('testo.txt')

def stampa_struttura(arrs , dict):
    print("-----STRUTTURA-----")
    for key, value in dict.items():
        print(key)
        for x in value:
            print_arr(arrs[x-1])

def conta(arrs, dict):
    ##stampa il gruppo che contiene più volte il numero 3
    max_counter = 0
    for key , value in dict.items():
        counter = 0
        for x in value: ## per ogni indice di array del gruppo
            i = 0
            while(i < len(arrs[x-1])):
                if(arrs[x-1][i] == 3):
                    counter += 1
                i += 1
        if counter > max_counter:
            max_counter = counter
            max_gruppo = key
    print("Il gruppo con più 3 è: ", end = ' ')
    print(max_gruppo)

## 2: stampare i gruppi da quelli che contengono più numeri pari a quelli
#che contengono meno numeri pari.


def duplicati(arrs):
    print("FUNZIONE DUPLICATI-")
    for arr in arrs:
        counter = {}
        for x in arr:
            if x in counter.keys():
                counter[x] += 1
            else:
                counter[x] = 1
        for key , value in counter.items():
            if(value != 1):
                print("Occorrenze di ", end = ' ')
                print("Nell'array: ", end = ' ')
                print(arr)
                print(key, end = ' ')
                print(": ",end = ' ')
                print(value)        

def ordina_pari(arrs , dict):
    print("stampo in ordine da chi contiene più numeri pari a chi meno: ")
    pari_counter  = []
    for arr in arrs:
        pari = 0
        for x in arr:
            if(x%2 == 0):
                pari +=1
        pari_counter.append(pari)
    pari_dict = {}
    for key , value in dict.items():
        n = 0
        for x in value: ## per ogni indice di ogni gruppo
            n += pari_counter[x-1]
        pari_dict[key] = n
    pari_dict = sorted(pari_dict.items() , key = lambda x:x[1], reverse = True)
    ##print(pari_dict) per debuggare può essere utile.
    for key in pari_dict:
        print(key[0])

arrs = [] ## contiene tutti gli array
while(True):
    temp = f.readline()
    if(temp == '\n'):
        break
    ##arrs = [[1,2,3,4][3,4,5][2,3,4]]
    ## dict: {A: 1,2; B:2} valori che puntano alle caselle di arrs
    ## presuppongo che gli ID degli array vadano da 1 a n
    str1 = temp[2:]
    str1 = str1.replace('\n', '')
    arr = list(str1.split(','))
    converti(arr)
    arrs.append(arr)
##ora creo il dizionario
dict = {}
while(True):
    temp = f.readline()
    if not temp:
        break
    key = temp[0]
    temp = temp[2:]
    temp = temp.replace('\n' , '')
    arr = list(temp.split(','))
    converti(arr)
    dict[key] = arr
stampa_struttura(arrs ,dict)
ordina_pari(arrs , dict)
