import matplotlib.pyplot as plt
import math
a = "1"
b = "" ##new value
leng = 30
x = [x for x in range(leng)]
y = []
current_counter = 0
for i in range (leng):
    j = 0
    while j < len(a):
        prev_value = a[j]
        while j != len(a) and prev_value ==a[j]:
            current_counter += 1
            j+=1
        b += str(current_counter) + str(prev_value)
        current_counter = 0
    y.append(int(len(b)))
    a = b
    b = ""


for k in range(len(y)):
    print(str(k) + ")" + str(y[k]))

plt.scatter(x,y, c = 'blue')



plt.show()