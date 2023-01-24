import matplotlib.pyplot as plt
import numpy as np

plt.figure()

plt.subplot(2, 2, 1)
width = 0.4
x_list = ["100mkM", "10mkM", "1 mkM", "0.1 mkM"]
y_D1 = [46.20, 31.4, 27.4, 40.7]
y_Control = [43.222, 53.25, 56.44, 50]
x_indexes = np.arange(len(x_list))
plt.xticks(x_indexes, ['100mkM', '10mkM', '1mkM', '0.1mkM'])
plt.title('platelet aggregation by Born')
plt.xlabel('concentration, %')
plt.ylabel('aggregation')

plt.bar(x_indexes - width/2, y_D1, label='D1', width=width)
plt.bar(x_indexes + width/2, y_Control, label='Control', width=width)
plt.legend()

plt.subplot(2, 2, 2)
width = 0.4
x_list = ["100mkM", "10mkM", "1 mkM", "0.1 mkM"]
y_D4 = [35.2, 42.4, 45.22, 36.11]
y_Control = [43.222, 53.25, 56.44, 50]

x_indexes = np.arange(len(x_list))
plt.xticks(x_indexes, ['100mkM', '10mkM', '1mkM', '0.1mkM'])
plt.xlabel('concentration, %')
plt.ylabel('aggregation')

plt.bar(x_indexes - width/2, y_D4, label='D4', width=width)
plt.bar(x_indexes + width/2, y_Control, label='Control', width=width)
plt.legend()

plt.subplot(2, 2, 3)
width = 0.4
x_list = ["100mkM", "10mkM", "1 mkM", "0.1 mkM"]
y_D7 = [40.04, 41.17, 35.13, 36.13]
y_Control = [43.222, 53.25, 56.44, 50]

x_indexes = np.arange(len(x_list))
plt.xticks(x_indexes, ['100mkM', '10mkM', '1mkM', '0.1mkM'])
plt.xlabel('concentration, %')
plt.ylabel('aggregation')

plt.bar(x_indexes - width/2, y_D7, label='D7', width=width)
plt.bar(x_indexes + width/2, y_Control, label='Control', width=width)
plt.legend()
plt.show()
