from matplotlib import pyplot as plt
import random
import math
import numpy

rollResults = []

for i in range(1, 1000000):
    dice1 = random.randint(1, 3)
    dice2 = random.randint(1, 3)
    result = dice1 + dice2
    rollResults.append(result)
customBins = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
plt.hist(rollResults, bins = customBins)
plt.show()
    




