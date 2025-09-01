'''
 2x + 5y + 2z = -38
 3x - 2y + 4z =  17
-6x +  y - 7z = -12
'''

constants = [
  [ 2,  5,  2, -38],
  [ 3, -2,  4,  17],
  [-6,  1, -7, -12]
]

a = [ 2,  5,  2, -38]
b = [ 3, -2,  4,  17]
c = [-6,  1, -7, -12]

a_1x = [i/a[0] for i in a]
b_1x = [i/b[0] for i in b]
c_1x = [i/c[0] for i in c]

a1x_minus_b1x = [i - j for i, j in list(zip(a_1x, b_1x))]
a1x_minus_c1x = [i - j for i, j in list(zip(a_1x, c_1x))]

a0x_b0x = a1x_minus_b1x[1:]
a0x_c0x = a1x_minus_c1x[1:]

a0x_b0x_1y = [i/a0x_b0x[0] for i in a0x_b0x]
a0x_c0x_1y = [i/a0x_c0x[0] for i in a0x_c0x]

a0xb0x1y_minus_a0xc0x1y = [
  i - j for i, j in list(zip(a0x_b0x_1y, a0x_c0x_1y))]

a0x0y_b0x0y_c0x0y = a0xb0x1y_minus_a0xc0x1y[1:]

# plug and solve
z = a0x0y_b0x0y_c0x0y[1]/a0x0y_b0x0y_c0x0y[0]
y = a0x_b0x_1y[2] - a0x_b0x_1y[1]*z
x = a_1x[3] - ((a_1x[1]*y) + (a_1x[2]*z))
(x, y, z)








