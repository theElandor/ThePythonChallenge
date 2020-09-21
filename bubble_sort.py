import random
def swap(list , pos1 , pos2):
    s = list[pos1]
    list[pos1] = list[pos2]
    list[pos2] = s     ## function to swap elelements of a list

def bubble_sort(nums):
    operations = 0
    ordered = False
    while ordered == False:
        operations = 0
        for i in range (len(nums)-1):
            if nums[i] > nums[i+1]:
                swap(nums,i,i+1)
                operations += 1
        if operations == 0:
            ordered = True
    print(nums)

nums = []
for x in range(100):
    nums.append(random.randint(1,10))
print(nums)
bubble_sort(nums)
