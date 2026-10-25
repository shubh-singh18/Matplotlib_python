import matplotlib.pyplot as plt
name=["ritika","prajjwal","shubh","shivam"]
marks=[40,35,29,45]
plt.scatter(name,marks,color="orange")
plt.title("student record",color="red")
plt.xlabel("student name",color="red")
plt.ylabel("student marks",color="red")
plt.grid(True)
plt.savefig("scatter_data1.png")
plt.show()
