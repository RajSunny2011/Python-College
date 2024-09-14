# Q7. Create a program to demonstrate different visual forms using Matplotlib.
import matplotlib.pyplot as plt
import numpy as np

# Line Plot
t = np.arange(0.0, 2.0, 0.01)
s = [np.sin(i*np.pi) for i in t]
plt.subplot(2, 2, 1)
plt.plot(t, s)
plt.title('Line Plot')
plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')

categories = ['Apples', 'Bananas', 'Cherries', 'Dates']
values = [15, 30, 45, 10]
# Bar Chart
plt.subplot(2, 2, 2)
bars = plt.bar(categories, values)
plt.title('Bar Chart')
plt.xlabel('Fruits')
plt.ylabel('Quantity')

# Pie Chart
plt.subplot(2, 2, 3)
plt.pie(values, labels=categories)
plt.title('Pie Chart')

# Histogram
plt.subplot(2, 2, 4)
data = np.random.randn(100)
plt.hist(data, bins=10)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
