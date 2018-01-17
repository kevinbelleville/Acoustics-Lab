A_0 = [
    0.0403,
    0.0276,
    0.01818,

]

thing = [
    0.00082543,
    0.00055694,
    0.00046199,

]

from math import *
import matplotlib.pyplot as plt

alpha = []

for i, A in enumerate(A_0):
    alpha.append(-thing[i]/log(A))


f = [0.65908,
1.8867,
2.8682,
]

def Q(alp, f):
    w = 2*pi*f
    return w/(2*alp)

Q_ = []
for i, a in enumerate(alpha):
    Q_.append(Q(a, f[i]))

plt.plot(f, Q_, "o")
plt.show()
