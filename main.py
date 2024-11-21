import numpy as np
import matplotlib.pyplot as plt


k = 8.99e9  # Константа электростатического взаимодействия (Н·м²/Кл²)

# Параметры зарядов (x, y, заряд)
charges = [
    (0.5, 0.5, 1e-3),
    (-0.5, -0.5, -1e-3),
    (0, 0, 1e-3),
]


x = np.linspace(-1, 1, 200)
y = np.linspace(-1, 1, 200)
X, Y = np.meshgrid(x, y)


Ex_total = np.zeros(X.shape)
Ey_total = np.zeros(Y.shape)


for cx, cy, q in charges:

    dx = X - cx
    dy = Y - cy


    r_squared = dx ** 2 + dy ** 2
    r_squared[r_squared == 0] = 1e-10
    r = np.sqrt(r_squared)


    Ex = k * q * dx / r_squared
    Ey = k * q * dy / r_squared


    Ex_total += Ex
    Ey_total += Ey

E_magnitude = np.sqrt(Ex_total ** 2 + Ey_total ** 2)

plt.figure(figsize=(10, 8))


plt.gca().set_facecolor('white')


cmap = plt.get_cmap('viridis')
norm = plt.Normalize(vmin=E_magnitude.min(), vmax=E_magnitude.max())
plt.pcolormesh(X, Y, E_magnitude, shading='auto', cmap=cmap, norm=norm, alpha=0.7)


plt.quiver(X[::10, ::10], Y[::10, ::10], Ex_total[::10, ::10], Ey_total[::10, ::10], scale=5e8, color='black')  # Уменьшили scale для увеличения длины векторов


for cx, cy, q in charges:
    color = 'red' if q > 0 else 'blue'
    plt.scatter(cx, cy, color=color, s=200, edgecolor='black', label=f'Q = {q:.1e} Кл')  # Увеличен размер маркеров

plt.xlabel('x (м)')
plt.ylabel('y (м)')
plt.title('Электростатическое поле трех зарядов')
plt.colorbar(label='|E| (Н/Кл)')
plt.legend()
plt.grid(False)
plt.axis('equal')


plt.savefig('result.png', format='png')


plt.show()
