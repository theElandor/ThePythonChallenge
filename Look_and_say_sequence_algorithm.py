##o(n^2) time compl i think
a = "1"
b = "" ##new value
current_counter = 0
for i in range (30):
    j = 0
    while j < len(a):
        prev_value = a[j]
        while j != len(a) and prev_value ==a[j]:
            current_counter += 1
            j+=1
        b += str(current_counter) + str(prev_value)
        current_counter = 0
    a = b
    b = ""
    print(str(i) + ")"+str(len(a)))





