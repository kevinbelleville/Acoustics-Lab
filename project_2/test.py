from math import *
import matplotlib.pyplot as plt

g = 9.81
h = 0.027
L = 0.375

def omega(k):
    ans = (g*k + sig_over_rho*k*k*k)*tanh(k*h)
    return sqrt(ans)

def omega_no_st(k):
    ans = (g*k)*tanh(k*h)
    return sqrt(ans)

def cph(k, w):
    return w/k

sig_over_rho = 4.30327*(10**(-5))

print("Grav, height cph =", str(sqrt(g*h)))

ns = [1,3,5,7,9,11,13,15,17,19]
wavenums = []

def wavenumber_gen(n):
    return n*pi/L

for n in ns:
    wavenums.append(wavenumber_gen(n))

measured = [
    0.65908,
    1.8867,
    2.8682,
    3.6369,
    4.259,
    4.7918,
    5.268,
    5.7115,
    6.1253,
    6.5479

]

print("n, k, w, measured w, diff, cph, mcph")

"""
for i, wave in enumerate(wavenums):
    mylist = [ns[i], wave, omega(wave)/(2*pi), measured[i], cph(wave, (omega(wave)/(2*pi))), cph(wave, measured[i])]
    print_string = ''
    for i, thing in enumerate(mylist):
        if i == 0 or i == 1:
            print_string += str(thing) + " "
        else:
            print_string += '%.4f' % thing + " "
    print(print_string)

for i, wave in enumerate(wavenums):
    print(str(ns[i])+" & "+str(wave)+" & "+str(measured[i])+" & "+str(cph(wave, measured[i]))+" \\\\")
    print("\\hline")
"""

## x = wavenums
y = []
st = []
nost = []
diff_st = []
diff_nost = []
for i,wave in enumerate(wavenums):
    a = cph(wave, (omega(wave)/(2*pi)))
    b = cph(wave, (omega_no_st(wave)/(2*pi)))
    c = cph(wave, measured[i])
    diff_st.append(a-c)
    diff_nost.append(b-c)



plt.plot(wavenums, diff_st, "ro", label="With Surface Tension")

plt.plot(wavenums, diff_nost, "bo", label="Without Surface Tension")

plt.legend()
plt.show()
