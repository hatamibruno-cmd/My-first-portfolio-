import math
import random
import matplotlib.pyplot as plt

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Data for a three dimensional line
    z_line = [i * 15 / 999 for i in range(1000)]
    x_line = [math.sin(z) for z in z_line]
    y_line = [math.cos(z) for z in z_line]
    ax.plot3D(x_line, y_line, z_line, 'red')

    # Data for three dimensional scattered points
    z_scatter = [15 * random.random() for _ in range(100)]
    x_scatter = [math.sin(z) + 0.1 * random.gauss(0, 1) for z in z_scatter]
    y_scatter = [math.cos(z) + 0.1 * random.gauss(0, 1) for z in z_scatter]
    ax.scatter3D(x_scatter, y_scatter, z_scatter, c=z_scatter, cmap='Greens')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Helix with Noisy Scatter')

    plt.show()

if __name__ == "__main__":
    main()
