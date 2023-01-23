import matplotlib.pyplot as plt

x_list = ["100mkM", "10mkM", "1 mkM", "0.1 mkM", "Control"]
y_D1 = [46.20, 31.4, 27.4, 40.7, 43.222]
y_D4 = [35.2, 42.4, 45.22, 36.11, 53.25]
y_D7 = [40.04, 41.17, 35.13, 36.13, 56.44]

plt.title('platelet aggregation by Born')
plt.xlabel('concentration, %')
plt.ylabel('aggregation')
plt.plot(x_list, y_D1, label='D1', marker='o')
plt.plot(x_list, y_D4, label='D4', marker='v')
plt.plot(x_list, y_D7, label='D7', marker='>')
plt.legend()
plt.show()
