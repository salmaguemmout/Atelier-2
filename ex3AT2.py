liste = [1, 2, 3, 1, 2, 3, 1, 2, 3]
comptes = {}
for element in liste:
  
  if element in comptes:
    comptes[element] += 1
  else:
    comptes[element] = 1
print(comptes)