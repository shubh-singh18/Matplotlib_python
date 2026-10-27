import  matplotlib.pyplot as plt
sales1=[1200,1300,1400,1500]
sales2=[1100,1300,1350,1560]
months=["jan","fed","mar","apl"]
plt.plot(months,sales1,label="sales1")
plt.plot(months,sales2,label="sales2")
plt.legend()
plt.grid()
plt.show()
