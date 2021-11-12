# Creating 3 different sized squares

import matplotlib.pyplot as plt


def small():
    x = [3, 3, 4, 4, 3]
    y = [3, 4, 4, 3, 3]
    plt.plot(x, y, 'r:o')


def medium():
    x = [2, 2, 5, 5, 2]
