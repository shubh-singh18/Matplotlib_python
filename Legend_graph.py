import matplotlib.pyplot as plt
flip=[1000,1200,1300,1400]
ama=[1000,1200,1250,1500]
months=["jan","fed","mar","april"]
plt.plot(months,ama,label="amazon")
plt.plot(months,flip,label="flip")
plt.legend()
plt.savefig("legend")
plt.show()   