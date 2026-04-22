import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# NumPy data
data = np.array([50, 60, 70, 80, 90])

# Pandas DataFrame
df = pd.DataFrame(data, columns=["Marks"])

print("Average Marks:", df["Marks"].mean())

# Plot
plt.plot(df["Marks"])
plt.title("Marks Analysis")
plt.show()
