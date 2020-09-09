import pyinputplus as pyip
def adds_up_to_ten(numbers):
    numberList = []
    for element in numbers:
        numberList.append(int(numbers))
    for i, digit in enumerate(numberList):
        numberList[i] = int(digit)
        if sum(numberList) != 10:
            raise Exception("The digits must add up to 10")
    return int(numbers)

response = pyip.inputCustom(adds_up_to_ten)