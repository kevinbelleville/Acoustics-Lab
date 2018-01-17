del_f = []
del_f.append(0.68909-0.63207)
del_f.append(1.9107-1.8447)
del_f.append(2.8982-2.8202)
del_f.append(3.6875-3.5923)
del_f.append(4.3185-4.2054)
del_f.append(4.8722-4.7293)

f = [0.65908,
1.8867,
2.8682,
3.6369,
4.259,
4.7918
]

import matplotlib.pyplot as plt

Q = []
for i,_ in enumerate(f):
    Q.append(_/del_f[i])

plt.plot(f, Q, "ro")
plt.show()
