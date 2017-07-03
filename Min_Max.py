lst = [1, 5, 3, 7, 0, 2]

max_elem = lst[0]
for number in range(len(lst)):
  if lst[number] > max_elem:
    max_elem = lst[number]
print max_elem

min_elem = lst[0]
for number in range(len(lst)):
  if lst[number] < min_elem:
    min_elem = lst[number]
print min_elem    
