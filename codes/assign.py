# importing modules
import numpy as np
import matplotlib.pyplot as plt
  
# creating dataset
data = [2,5,7,9,10,13,14,17,17,19,134,33,33,37,35,39,38,35,35,34,33,34,35,40,43,42,43,47,45,44,45,43,45,48,48,49,42,43,46,45,43,45,47,41,42,41,40,44,46,50,50,53,52,53,55,57,56,51,50,50,52,53,57,57,50,60,62,60,67,68,64,63,60,62,68,67,70,77,75,73,70,79,80,88,84,82,91,99,93]
  
# creating class interval
classInterval = [400, 450, 500, 550, 600, 650, 700]
  
# calculating frequency and class interval
values, base = np.histogram(data, bins=classInterval)
  
# calculating cumulative sum
cumsum = np.cumsum(values)
  
# plotting  the ogive graph
plt.plot(base[1:], cumsum, color='red' , marker='o', linestyle='-')
  
# formatting
plt.title('Ogive Graph')
plt.xlabel('Number of students')
plt.ylabel('Cumulative Frequency')