import matplotlib.pyplot as plt
name=["ritika","prajjwal","shubh","shivam"]
marks=[40,35,29,45]
color=["pink","black","orange","red"]
plt.pie(marks,labels=name,colors=color,autopct="%1.f%%")
plt.savefig("Pie_chart")
plt.show()
