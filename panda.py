import matplotlib.pyplot as plt
import pandas as pd

stud_data ={
	"name":["kunal","jayesh","sam","sonya"],
	"age":[8,20,21,15]}

data=pd.DataFrame(stud_data)


a=data.groupby('name')['age'].sum()

plt.figure()
plt.bar(a.index ,a.values)
plt.xlabel("Age")
plt.ylabel("size")
plt.title("graph")
plt.show()



plt.figure()
plt.pie(a.values ,autopct="%1.1f%%")
plt.xlabel("Age")
plt.ylabel("size")
plt.title("graph")
plt.show()


plt.figure()
plt.scatter(a.index ,a.values)
plt.xlabel("x")
plt.ylabel("y")
plt.show()


plt.figure()
plt.plot(a.index ,a.values)
plt.xlabel("x")
plt.ylabel("y")
plt.show()





import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales_data.csv")
print(data)

d = data.groupby('Category')['Price'].sum()
print(d)

total = data['Stock'].sum()
print("Total Stock:", total)

print(data.describe())
print(data.mean(numeric_only=True))

d.plot(kind="line", marker="s")
plt.plot(d.index, d.values, marker="s")
plt.grid(True)

plt.show()







