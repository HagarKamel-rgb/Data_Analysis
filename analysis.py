import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"E:\pythonnn\DataAnalysis\tips.csv")
print(df.head())

df.dropna(inplace=True)

print("Total Tips:", df["tip"].sum())
print("Average Tip:", df["tip"].mean())

print("Tips by Day:")
print(df.groupby("day")["tip"].sum())

df.groupby("day")["tip"].sum().plot(kind='bar')
plt.title("Total Tips by Day")
plt.show()

df.groupby("sex")["tip"].sum().plot(kind='bar')
plt.title("Tips by Gender")
plt.show()

plt.scatter(df["total_bill"], df["tip"])
plt.title("Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()