def print_triangle_sides(triangles):
  for i, triangle in enumerate(triangles):
    triangle.sort()
    if i % 3 == 0:
      print(triangle[0])
    elif i % 3 == 1:
      print(triangle[1])
    else:
      print(triangle[2])

n = input('Enter the number of triangles : ')
triangles = []
for i in range(int(n)):
    a,b,c = map(int, input().split(' '))
    triangles.append([a,b,c])

print_triangle_sides(triangles)