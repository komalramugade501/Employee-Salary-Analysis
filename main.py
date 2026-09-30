import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Employee": ["Amit", "Neha", "Priya", "Rahul", "Rohan"],
    "Salary": [30000, 45000, 50000, 35000, 40000],
}

df = pd.DataFrame(data)

print("Employee Salary Data")
print(df.to_string(index=False))
print("\nAverage Salary:", df["Salary"].mean())
print("Minimum Salary:", df["Salary"].min())
print("Maximum Salary:", df["Salary"].max())

plt.figure(figsize=(8, 5))
plt.bar(df["Employee"], df["Salary"])
plt.title("Employee Salary Comparison")
plt.xlabel("Employee")
plt.ylabel("Salary")
plt.tight_layout()
plt.savefig("salary_comparison.png", dpi=150)
plt.show()
