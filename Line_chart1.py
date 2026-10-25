import matplotlib.pyplot as plt
marks=[70,80,60,89]
name=["prajjwal","shubh","shivam","devansh"]
plt.plot(marks,name,color="red",linestyle=":",marker="*")
plt.title("student record",color="red")
plt.xlabel("Student marks",color="red")
plt.ylabel("student name",color="red")

plt.grid(True)
plt.savefig("line_chart")
plt.show()