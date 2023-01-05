#Part 1 Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
numbers = []
with open("day-01/day1input.txt") as f:
    for line in f:
        numbers.append(line.strip())

inputList = []
currentList = []
for number in numbers:
    if not number:

        inputList.append(currentList)
        currentList = []
    else:

        currentList.append(number)

inputList.append(currentList)
elfCaloriesList = []

elfCaloriesList = inputList

def strToIntForNestedList(elf_calories: list) -> list:

    return [[int(x) for x in inner_list] for inner_list in elf_calories]
intValueOfList = strToIntForNestedList(elfCaloriesList)
def highestSum(intValueOfList):
  highestSum = 0
  for sublist in intValueOfList:
    sum = 0
    for element in sublist:
      sum += element
    if sum > highestSum:
      highestSum = sum
  return highestSum
print("The total calories : ", highestSum(intValueOfList))
#Part 2 Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
def findLargestSums(intValueOfList):
  sums = []
  for sublist in intValueOfList:
    sumOfNumber = 0
    for number in sublist:
      sumOfNumber += number
    sums.append(sumOfNumber)
  sortedSums = sorted(sums, reverse=True)
  largestThree = sortedSums[:3]
  for sumOfNumber in largestThree:
    print(sumOfNumber)
  total = sum(largestThree)
  print("Total sum of top three Elves carrying the most Calories : ",total)
findLargestSums(intValueOfList)
