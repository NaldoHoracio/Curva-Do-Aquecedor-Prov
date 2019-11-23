import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.array([0.3, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5])
y = np.array([23.4, 27.9, 34.0, 42.9, 56.2, 72.3, 91.8, 107.6, 132.7])

coefs = np.polyfit(x,y,1)

y_fit = coefs[0] * x + coefs[1]
y_residue = y - y_fit
sq_resid = sum(pow(y_residue,2))
sq_total = len(y) * np.var(y)

print("Coef angular: ", coefs[0])
print("Coef linear: ", coefs[1])
print("Equação da reta:")
print("T(v) =  ", coefs[0], "* v ", coefs[1])
print("T - temperatura em graus Celcius")
print("v - tensão em voltz")

plt.plot(x,y,'o')
plt.plot(x,np.polyval(coefs,x), 'g--')
plt.title('Equação da reta Tensão X Temperatura')
plt.legend(['T(v) = 26.462882402469816 * v - 0.146919730564098'])
plt.xlabel("Tensão (V)")
plt.ylabel("Temperatura (°C)")
plt.show()

