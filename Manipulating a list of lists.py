
def printTable(x):
    max = 0
    maxes = []
    for i in range (len(x)):
        for j in range(len(x[i])):
            l = len(x[i][j])
            if l > max:
                max = l
        maxes.append(max)
        max = 0
    return maxes

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
nums = printTable(tableData)
##nums = [8,5,5]
print(nums)
max = 0
for x in nums:
    if x > max:
        max = x

for x in range(len(tableData[0])):
    for list in tableData:
        print(list[x].rjust(max),end = " ")
    print("")

