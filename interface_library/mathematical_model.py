import pandas as pd
from scipy.integrate import odeint
import numpy as np
from matplotlib import pyplot as plt

# concentrations
Ca0 = 0.3
Cx0 = 0.4  # let x = A.E
Ce0 = 0.2
Cr0 = 0

# kinetic constants
k1 = 1
k2 = 2
k3 = 3

# rates of reaction


def r1(k1, Ca, Ce):
    return k1*Ca*Ce


def r2(k2, Cx):
    return k2*Cx


def r3(k2, k3, Cx):
    return (k3 + k2)*Cx


def r4(k3, Cx):
    return k3*Cx


time = np.linspace(0, 5)


def dSdt(time, S):
    Ca, Ce, Cr = S
    return [-r1(k1, Ca, Ce) + r2(k2, Ce),
            -r1(k1, Ca, Ce) + r3(k2, k3, Cx0),
            r4(k3, Cx0)
            ]


S_0 = (Ca0, Ce0, Cr0)
sol_1 = odeint(dSdt, y0=S_0, t=time, tfirst=True)
df = pd.DataFrame(sol_1)
df.plot()
plt.show()