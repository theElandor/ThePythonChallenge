string = "common sense is not so common"
encripted = ""
key = 8
for i in range (0,key):
    j = i
    while j < len(string):
        encripted = encripted + string[j]
        j += 8
print(encripted)
