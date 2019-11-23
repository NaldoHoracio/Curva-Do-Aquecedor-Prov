import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.array([0.3, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5])
y = np.array([23.4, 27.9, 34.0, 42.9, 56.2, 72.3, 91.8, 107.6, 132.7])

arr = np.polyfit(x,y,1)

y_fit = arr[0] * x + arr[1]
y_residue = y - y_fit
sq_resid = sum(pow(y_residue,2))
sq_total = len(y) * np.var(y)
r2 = 1 - sq_resid/sq_total

print(arr)
print(r2)

plt.plot(x,y,'o')
plt.plot(x,np.polyval(arr,x), 'g--')
plt.title('Equação da reta Tensão X Temperatura')
plt.xlabel("Tensão (V)")
plt.ylabel("Temperatura (°C)")
plt.show()

