import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Read Excel files
train = pd.read_excel(r"training_set.xlsx")
test = pd.read_excel(r"test.xlsx")

# -----------------------------
# TRAINING DATA
# -----------------------------

x_train = train["YObs(Train)"]
y_train = train["YPred(MLR model)"]

# Calculate R2 for training
r_train = linregress(x_train, y_train).rvalue
R2_train = r_train**2

# -----------------------------
# TEST DATA
# -----------------------------

x_test = test["YObs(Test)"]
y_test = test["YPred(Test)"]

# Calculate R2 for test
r_test = linregress(x_test, y_test).rvalue
R2_test = r_test**2

# -----------------------------
# COMBINED PLOT
# -----------------------------

plt.figure(figsize=(8,7))

# Training points
plt.scatter(x_train,
            y_train,
            color='red',
            s=70,
            label=f'Training Set (R² = {R2_train:.3f})')

# Test points
plt.scatter(x_test,
            y_test,
            color='blue',
            s=70,
            label=f'Test Set (R² = {R2_test:.3f})')

# Regression line for training
m1, b1 = np.polyfit(x_train, y_train, 1)

plt.plot(x_train,
         m1*x_train + b1,
         color='red',
         linewidth=2)

# Regression line for test
m2, b2 = np.polyfit(x_test, y_test, 1)

plt.plot(x_test,
         m2*x_test + b2,
         color='blue',
         linewidth=2)

# Ideal line y = x
all_x = np.concatenate([x_train, x_test])

plt.plot([min(all_x), max(all_x)],
         [min(all_x), max(all_x)],
         linestyle='--',
         color='black',
         linewidth=2,
         label='Ideal Line')

# Labels and title
plt.xlabel("Observed Activity", fontsize=12)
plt.ylabel("Predicted Activity", fontsize=12)

plt.title("Training and Test Set Regression Plot", fontsize=14)

# Legend
plt.legend()

# Grid
plt.grid(True)

# Show plot
plt.show()