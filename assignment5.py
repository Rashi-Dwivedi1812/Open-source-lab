import numpy as np
X = np.linspace(-np.pi, np.pi, 256, endpoint=True) 
C, S = np.cos(X), np.sin(X)
import matplotlib.pyplot as plt
plt.plot(X, C)
plt.plot(X, S)
plt.show()

plt.figure(figsize=(8, 6), dpi=80)
plt.subplot(1, 1, 1)
plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-")
plt.plot(X, S, color="green", linewidth=1.0, linestyle="-")
plt.xlim(-4.0, 4.0)
plt.xticks(np.linspace(-4, 4, 9, endpoint=True))
plt.ylim(-1.0, 1.0)
plt.yticks(np.linspace(-1, 1, 5, endpoint=True))
plt.savefig("exercise_2.png", dpi=72)
plt.show()

plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-", label="sine")
plt.legend(loc='upper left')
plt.show()

n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2 * X)
plt.plot(X, Y + 1, color='blue', alpha=1.00)
plt.plot(X, Y - 1, color='blue', alpha=1.00)
plt.show()

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
plt.scatter(X,Y)
plt.show()

n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.show()
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
plt.show()

x = np.array([-np.pi, -np.pi/4, -np.pi/2, 0, np.pi/4, np.pi/2, np.pi])

tan_x = np.tan(x)
cot_x = 1 / np.tan(x)
sec_x = 1 / np.cos(x)
cosec_x = 1 / np.sin(x)

plt.plot(x, tan_x, 'r-', label='tan(x)')
plt.plot(x, cot_x, 'g--', label='cot(x)')
plt.plot(x, sec_x, 'b-.', label='sec(x)')
plt.plot(x, cosec_x, 'm:', label='cosec(x)')

plt.legend()
plt.grid(True)
plt.title("Trigonometric Functions")
plt.xlabel("x values (radians)")
plt.ylabel("Function values")
plt.show()

methods = ['A', 'B', 'C', 'D']
result1 = [2, 5, 8, 5]
result2 = [3, 2, 5, 7]

x = np.arange(len(methods))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
bars1 = ax.bar(x - width/2, result1, width, label='Result1', color='skyblue')
bars2 = ax.bar(x + width/2, result2, width, label='Result2', color='salmon')

# Add labels and title
ax.set_xlabel('Method')
ax.set_ylabel('Values')
ax.set_title('Comparison of Result1 and Result2 by Method')
ax.set_xticks(x)
ax.set_xticklabels(methods)
ax.legend()

plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()