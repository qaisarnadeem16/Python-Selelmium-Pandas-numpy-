import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8]
y=[o*o for o in x]
plt.subplot(1,2,1)
plt.plot(x,y , color='pink')

plt.subplot(1, 2, 2)
plt.plot(x, y, color='green')
plt.show()