import numpy as np
a_matris = [[1,0,0],
[0,1,0],
[0,0,1]]

x_matris = []
b_matris = [2, 4, 9]

u_a_matris = np.triu(a_matris)

x3 = float(b_matris[2])/u_a_matris[2][2]
x2 = float(b_matris[1] - x3*u_a_matris[1][2])/u_a_matris[1][1]
x1 = float(b_matris[0] - x2*u_a_matris[0][1] - x3*u_a_matris[0][2])/u_a_matris[0][0]

print(x1, x2, x3)
