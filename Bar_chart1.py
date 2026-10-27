import matplotlib.pyplot as plt
name=["shubh","shivam","ram","shiva"]
marks=[90,89,78,79]
plt.yticks(range(0,120,20))
plt.ylim(0,100)
plt.bar (name,marks,color="black")
plt.title("Student Record",color="red")
plt.xlabel("Name",color="purple")
plt.ylabel("Marks",color="purple")
plt.show()
