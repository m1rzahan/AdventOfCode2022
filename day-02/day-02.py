#Part 1 What would your total score be if everything goes exactly according to your strategy guide?
scores = {
  ('B', 'X'): 1,
  ('A', 'Y'): 8,
  ('C', 'Z'): 6,
  ('B', 'Y'): 5,
  ('B', 'Z'): 9,
  ('A', 'X'): 4,
  ('A', 'Z'): 3,
  ('C', 'X'): 7,
  ('C', 'Y'): 2
}
with open("day2input.txt") as f:
  totalScsore = 0
  for line in f:
   characters = list(line.split())
   for a, b in zip(characters[::2], characters[1::2]):
    if (a, b) in scores:
     totalScsore += scores[(a, b)]
    print(totalScsore)

