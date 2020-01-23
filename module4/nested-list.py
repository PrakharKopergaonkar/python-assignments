#nested list comprehension
matrix = []
for i in range(5):
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)
matrix1 = [[i for i in range(5)] for j in range(5)]
print(matrix)
print(matrix1)

#flatten 2-d matrix into 1-d matrix
matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
flatten_matrx=[]
for sublist in matrix2:
    for val in sublist:
        flatten_matrx.append(val)
print(flatten_matrx)
flatten_matrx2 = [val for sublist in matrix2 for val in sublist]
print(flatten_matrx2)

#nested list comprehension with an if conditions
planet = [['mercury', 'venus', 'earth'],['mars', 'jupyter', 'saturn'],['uranus', 'neptune', 'pluto']]
flatten_planet = [planet for sublist in planet for planet in sublist if len(planet)<6]
print(flatten_planet)
