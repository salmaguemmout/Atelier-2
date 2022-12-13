l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]
l3 = []
for i, e in enumerate(l1):

  if i % 2 != 0:
    l3.append(e)
for i, e in enumerate(l2):
  
  if i % 2 == 0:
    l3.append(e)
print(l3)