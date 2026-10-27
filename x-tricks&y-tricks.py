# import matplotlib.pyplot as plt
# months=[1,2,3,4,5,6,9]
# sales=[1250,1300,1350,1234,1000,1200,1232]
# plt.plot(months,sales)
# plt.xticks([1,2,3,4,5,6,9],["jan","fed","march","april","may","june","september"])
# plt.yticks([900,1000,1200,1250,1500])
# plt.show()


# xlim
import matplotlib.pyplot as plt
months=[1,2,3,4,5,6,9]
sales=[1250,1300,1350,1234,1000,1200,1232]
plt.xticks(range(0,13,3))
plt.xlim(0,12)
plt.plot(months,sales)
plt.show()

